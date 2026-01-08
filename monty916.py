import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "KNN (k=5)": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42)
}
def calculate_metrics(model, X, y):
    y_pred = model.predict(X)
    return {
        "accuracy": accuracy_score(y, y_pred),
        "precision": precision_score(y, y_pred, average="macro"),
        "recall": recall_score(y, y_pred, average="macro"),
        "f1": f1_score(y, y_pred, average="macro")
    }
results = []

for name, model in models.items():
    model.fit(X_train, y_train)

    train_metrics = calculate_metrics(model, X_train, y_train)
    test_metrics = calculate_metrics(model, X_test, y_test)

    results.append({
        "Model": name,
        "Train Accuracy": train_metrics["accuracy"],
        "Test Accuracy": test_metrics["accuracy"],
        "Train Precision": train_metrics["precision"],
        "Test Precision": test_metrics["precision"],
        "Train Recall": train_metrics["recall"],
        "Test Recall": test_metrics["recall"],
        "Train F1": train_metrics["f1"],
        "Test F1": test_metrics["f1"]
    })
    df_results = pd.DataFrame(results)
    print(df_results.round(3))

    #Raport: Porównanie klasyfikatorów – uczenie i overfitting
# Zbiór danych

#Do eksperymentu wykorzystano zbiór Iris (150 próbek, 3 klasy, 4 cechy).
#Jest to klasyczny, niewielki zbiór danych często używany do porównywania algorytmów klasyfikacji.

# Podział danych

#Zbiór treningowy: 70% danych

#Zbiór testowy: 30% danych

#Podział wykonano losowo z zachowaniem proporcji klas (stratified split).

# Użyte klasyfikatory

#Wybrano kilka popularnych klasyfikatorów:

#Regresja logistyczna

#k-Nearest Neighbors (k = 5)

#Drzewo decyzyjne

#Random Forest

# Metryki oceny

#Dla każdego modelu obliczono metryki:

#Accuracy (dokładność)

#Precision (precyzja, macro)

#Recall (czułość, macro)

#F1-score (macro)

#Metryki zostały policzone osobno dla zbioru treningowego i testowego.

#5. Wyniki
#Klasyfikator	Accuracy (train)	Accuracy (test)
#Regresja logistyczna	0.97	0.93
#KNN (k=5)	0.97	0.98
#Drzewo decyzyjne	1.00	0.93
#Random Forest	1.00	0.89

#(Pozostałe metryki – precision, recall, F1 – były zbliżone do accuracy i prowadzą do tych samych wniosków.)

#6. Wnioski
# Regresja logistyczna

#Bardzo dobre wyniki na zbiorze treningowym i testowym

#Niewielka różnica między train i test

#Model dobrze generalizuje, brak overfittingu

# KNN (k = 5)

#Najlepszy wynik na zbiorze testowym

#Bardzo podobne wyniki na obu zbiorach

#Model stabilny, bardzo dobra generalizacja
# Drzewo decyzyjne
#Idealne dopasowanie do danych treningowych (100%)

#Wyraźnie gorszy wynik na zbiorze testowym

#Oznaki overfittingu – model zbyt dobrze dopasował się do danych treningowych
# Random Forest

#Idealne wyniki na treningu

#Najgorszy wynik na zbiorze testowym spośród badanych modeli

#Silny overfitting (prawdopodobnie zbyt mały zbiór danych względem złożoności modelu)

# Podsumowanie końcowe

#Prostsze modele (regresja logistyczna, KNN) lepiej generalizują na małych zbiorach danych

#Modele drzewiaste bez ograniczeń łatwo overfittują

#Wysoka skuteczność na zbiorze treningowym nie gwarantuje dobrego działania na danych testowych
