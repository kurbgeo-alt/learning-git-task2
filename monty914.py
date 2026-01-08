#Problem regresji
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import OneHotEncoder, StandardScaler, PowerTransformer
from sklearn.decomposition import TruncatedSVD

from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
X = bike_data[numeric_features + categorical_features].copy()
y = bike_data[target].copy()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)
numeric_transformer = Pipeline(steps=[
    ('power', PowerTransformer()),
    ('scaler', StandardScaler())
])
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)
final_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('pca', TruncatedSVD(random_state=42)),
    ('regressor', ElasticNet(max_iter=10000))
])
params = {
    'pca__n_components': [10, 20, 50, 100],
    'regressor__alpha': [1e-4, 1e-3, 1e-2, 1e-1, 1, 10],
    'regressor__l1_ratio': np.arange(0, 1.1, 0.1)
}

grid = GridSearchCV(
    final_pipeline,
    params,
    scoring='neg_mean_squared_error',
    cv=5,
    n_jobs=-1
)

grid.fit(X_train, y_train)
print("Najlepsze parametry:")
print(grid.best_params_)
best_model = grid.best_estimator_

predictions = best_model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print(f"RMSE: {rmse:.4f}")
#Problem klasyfikacji
from sklearn.pipeline import Pipeline
from sklearn.decomposition import TruncatedSVD
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
rf_pipeline = Pipeline(steps=[
    ('pca', TruncatedSVD(random_state=42)),
    ('rf', RandomForestClassifier(
        n_estimators=1000,
        n_jobs=-1,
        random_state=42
    ))
])
params_rf = {
    'pca__n_components': [10, 20, 50, 100],
    'rf__max_depth': [3, 5, 10, 20],
    'rf__min_samples_leaf': [3, 5, 10, 15]
}

rf_gridsearch = GridSearchCV(
    rf_pipeline,
    params_rf,
    scoring='f1_macro',
    cv=5,
    verbose=10,
    n_jobs=-1
)

rf_gridsearch.fit(X_train, y_train)