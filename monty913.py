import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Dane(przykład)

# Przykładowy zbiór danych
df = pd.DataFrame({
    'feature_1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'feature_2': [2, 1, 4, 3, 5, 7, 6, 8, 9, 10],
    'target':    [3, 4, 6, 8, 9, 11, 13, 14, 16, 18]
})


# X i y

X = df[['feature_1', 'feature_2']]  # cechy
y = df['target']                    # zmienna docelowa


# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Modelowanie

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predykcje
y_predict_train = lr_model.predict(X_train)
y_predict_test = lr_model.predict(X_test)


# Metryki

mae_train = mean_absolute_error(y_train, y_predict_train)
rmse_train = np.sqrt(mean_squared_error(y_train, y_predict_train))
r2_train = r2_score(y_train, y_predict_train)

mae_test = mean_absolute_error(y_test, y_predict_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_predict_test))
r2_test = r2_score(y_test, y_predict_test)


# Wyniki

print("TRAIN:")
print(f"MAE:  {mae_train:.3f}")
print(f"RMSE: {rmse_train:.3f}")
print(f"R²:   {r2_train:.3f}")

print("\nTEST:")
print(f"MAE:  {mae_test:.3f}")
print(f"RMSE: {rmse_test:.3f}")
print(f"R²:   {r2_test:.3f}")