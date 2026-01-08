import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
X_train, X_test, y_train, y_test = train_test_split(
    X_text,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.9
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
rf = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train_vec, y_train)
importances = rf.feature_importances_
feature_names = np.array(vectorizer.get_feature_names_out())

importance_df = pd.DataFrame({
    "feature": feature_names,
    "importance": importances
})
selected_features = importance_df[
    importance_df["importance"] > 0.001
]["feature"]

selected_indices = np.where(
    np.isin(feature_names, selected_features)
)[0]

X_train_sel = X_train_vec[:, selected_indices]
X_test_sel = X_test_vec[:, selected_indices]
param_grid = {
    "n_estimators": [200, 400],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2]
}

rf_final = RandomForestClassifier(
    random_state=42,
    n_jobs=-1
)

grid = GridSearchCV(
    rf_final,
    param_grid,
    cv=5,
    scoring="f1_macro",
    n_jobs=-1
)

grid.fit(X_train_sel, y_train)
best_model = grid.best_estimator_

y_pred = best_model.predict(X_test_sel)

print("Najlepsze parametry:")
print(grid.best_params_)

print("\nRaport klasyfikacji:")
print(classification_report(y_test, y_pred))