import os
import datetime as dt
import pandas as pd

import dash
from dash import dcc, html
from dash.dependencies import Input, Output

import plotly.graph_objects as go

# =========================
# BAZA DANYCH
# =========================

class DB:
    def __init__(self):
        self.transactions = self.transaction_init()
        self.cc = pd.read_csv("db/country_codes.csv", index_col=0)
        self.customers = pd.read_csv("db/customers.csv", index_col=0)
        self.prod_info = pd.read_csv("db/prod_cat_info.csv")
        self.merge()

    @staticmethod
    def transaction_init():
        transactions = pd.DataFrame()
        src = "db/transactions"

        for filename in os.listdir(src):
            transactions = pd.concat(
                [transactions, pd.read_csv(os.path.join(src, filename), index_col=0)]
            )

        def convert_dates(x):
            for fmt in ("%d-%m-%Y", "%d/%m/%Y"):
                try:
                    return dt.datetime.strptime(x, fmt)
                except:
                    pass

        transactions["tran_date"] = transactions["tran_date"].apply(convert_dates)
        return transactions

    def merge(self):
        df = self.transactions.copy()

        df = df.join(
            self.prod_info.drop_duplicates("prod_cat_code")
            .set_index("prod_cat_code")["prod_cat"],
            on="prod_cat_code",
        )

        df = df.join(
            self.prod_info.drop_duplicates("prod_sub_cat_code")
            .set_index("prod_sub_cat_code")["prod_subcat"],
            on="prod_subcat_code",
        )
        df = df.join(
            self.customers.join(self.cc, on="country_code")
            .set_index("customer_Id"),
            on="cust_id",
        )

        self.merged = df


db = DB()
df = db.merged

# APP


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Tabs(
            id="tabs",
            value="tab-1",
            children=[
                dcc.Tab(label="Sprzedaż globalna", value="tab-1"),
                dcc.Tab(label="Produkty", value="tab-2"),
            ],
        ),
        html.Div(id="tabs-content"),
    ]
)


# TAB RENDERING


def render_tab1(df):
     return html.Div(
        [
            html.H1("Sprzedaż globalna", style={"textAlign": "center"}),
            dcc.DatePickerRange(
                id="sales-range",
                start_date=df["tran_date"].min(),
                end_date=df["tran_date"].max(),
                display_format="YYYY-MM-DD",
            ),
            html.Div(
                [
                    dcc.Graph(id="bar-sales", style={"width": "50%"}),
                    dcc.Graph(id="choropleth-sales", style={"width": "50%"}),
                ],
                style={"display": "flex"},
            ),
        ]
        )


def render_tab2(df):
    grouped = df[df["total_amt"] > 0].groupby("prod_cat")["total_amt"].sum()

    fig = go.Figure(
        data=[go.Pie(labels=grouped.index, values=grouped.values)],
        layout=go.Layout(title="Udział grup produktów"),
    )
    return html.Div(
        [
            html.H1("Produkty", style={"textAlign": "center"}),
            html.Div(
                [
                    dcc.Graph(figure=fig, style={"width": "50%"}),
                    html.Div(
                        [
                            dcc.Dropdown(
                                id="prod-dropdown",
                                options=[
                                    {"label": x, "value": x}
                                    for x in df["prod_cat"].dropna().unique()
                                ],
                                value=df["prod_cat"].dropna().unique()[0],
                            ),
                            dcc.Graph(id="barh-prod-subcat"),
                        ],
                        style={"width": "50%"},
                    ),
                ],
                style={"display": "flex"},
            ),
        ]
    )

   

                            


@app.callback(Output("tabs-content", "children"), Input("tabs", "value"))
def render_content(tab):
    if tab == "tab-1":
        return render_tab1(df)
    elif tab == "tab-2":
        return render_tab2(df)


# CALLBACKS TAB 1


@app.callback(
    Output("bar-sales", "figure"),
    Input("sales-range", "start_date"),
    Input("sales-range", "end_date"),
)
def bar_sales(start, end):
    truncated = df[(df["tran_date"] >= start) & (df["tran_date"] <= end)]

    grouped = (
        truncated[truncated["total_amt"] > 0]
        .groupby([pd.Grouper(key="tran_date", freq="M"), "Store_type"])["total_amt"]
        .sum()
        .unstack()
        .fillna(0)
    )

    fig = go.Figure()

    for col in grouped.columns:
        fig.add_bar(name=col, x=grouped.index, y=grouped[col])

    fig.update_layout(barmode="stack", title="Przychody")
    return fig


@app.callback(
    Output("choropleth-sales", "figure"),
    Input("sales-range", "start_date"),
    Input("sales-range", "end_date"),
)
def choropleth_sales(start, end):
    truncated = df[(df["tran_date"] >= start) & (df["tran_date"] <= end)]

    grouped = (
        truncated[truncated["total_amt"] > 0]
        .groupby("country")["total_amt"]
        .sum()
    )

    fig = go.Figure(
        go.Choropleth(
            locations=grouped.index,
            locationmode="country names",
            z=grouped.values,
            colorscale="Viridis",
        )
    )

    fig.update_layout(title="Mapa sprzedaży")
    return fig
# CALLBACKS TAB 2


@app.callback(
    Output("barh-prod-subcat", "figure"),
    Input("prod-dropdown", "value"),
)
def barh_prod_subcat(cat):
    grouped = (
        df[(df["total_amt"] > 0) & (df["prod_cat"] == cat)]
        .pivot_table(
            index="prod_subcat",
            columns="Gender",
            values="total_amt",
            aggfunc="sum",
        )
        .fillna(0)
    )

    fig = go.Figure()

    for gender in grouped.columns:
        fig.add_bar(
            x=grouped[gender],
            y=grouped.index,
            orientation="h",
            name=gender,
        )

    fig.update_layout(barmode="stack", title="Sprzedaż wg podkategorii")
    return fig



# START

if __name__ == "__main__":
    app.run_server(debug=True)
