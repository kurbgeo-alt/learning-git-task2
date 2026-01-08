import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Załadowanie danych (przykładowe dane)
data = pd.read_csv('path_to_data.csv')  # Załaduj dane z pliku CSV

# Preprocessing: skalowanie danych
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# 1. Klasterowanie KMeans (wstępne wybranie liczby klastrów)
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)

# Wizualizacja metody łokcia
plt.plot(range(1, 11), inertia)
plt.xlabel('Liczba klastrów')
plt.ylabel('Inertia')
plt.title('Metoda łokcia dla KMeans')
plt.show()

# Trening KMeans z wybraną liczbą klastrów (np. 4)
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(data_scaled)

# Wizualizacja wyników KMeans
pca = PCA(n_components=2)
pca_result = pca.fit_transform(data_scaled)

plt.scatter(pca_result[:, 0], pca_result[:, 1], c=clusters, cmap='viridis')
plt.title('Wyniki KMeans')
plt.show()

# 2. Klasterowanie DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_clusters = dbscan.fit_predict(data_scaled)

# Wizualizacja wyników DBSCAN
plt.scatter(pca_result[:, 0], pca_result[:, 1], c=dbscan_clusters, cmap='viridis')
plt.title('Wyniki DBSCAN')
plt.show()

# 3. Klasyfikacja nadzorowana
# Załóżmy, że mamy etykiety (labels) do klasyfikacji
labels = pd.read_csv('path_to_labels.csv')  # Załaduj etykiety

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(data_scaled, labels, test_size=0.2, random_state=42)

# Random Forest
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# SVM
svm = SVC(random_state=42)
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)

# Ewaluacja modeli
print("Random Forest Classification Report:")
print(classification_report(y_test, y_pred_rf))

print("SVM Classification Report:")
print(classification_report(y_test, y_pred_svm))




