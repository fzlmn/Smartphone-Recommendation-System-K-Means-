# ------------------------------
#  1. Importer les librairies
# ------------------------------
import pandas as pd                          # pour lire et manipuler le fichier Excel
import numpy as np                           # pour les calculs
import matplotlib.pyplot as plt              # pour tracer le graphique de la méthode du coude
from sklearn.preprocessing import StandardScaler  # pour normaliser les données
from sklearn.cluster import KMeans           # algorithme K-Means
from sklearn.metrics import pairwise_distances_argmin_min

# ------------------------------
#  2. Charger les données
# ------------------------------
# Remplace 'smartphones.xlsx' par le nom de ton fichier
df = pd.read_excel('smartphones.xlsx')

print("Aperçu de la base de données :")

# ------------------------------
#  3. Préparer et normaliser les données
# ------------------------------
# On garde uniquement les colonnes numériques utiles pour le clustering
X = df[['Prix', 'Autonomie', 'Camera']].values

# Normalisation (important pour que toutes les colonnes aient le même poids)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ------------------------------
#  4. Trouver le meilleur K (méthode du coude)
# ------------------------------
inertias = []  # inertie = erreur globale pour chaque K

# On teste K entre 1 et 10
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=0)
    model.fit(X_scaled)
    inertias.append(model.inertia_)  # on garde l'erreur de chaque modèle

# Tracer la courbe du coude
plt.figure(figsize=(6, 4))
plt.plot(range(1, 11), inertias, marker='o')
plt.title("Méthode du coude pour choisir K")
plt.xlabel("Nombre de clusters (K)")
plt.ylabel("Inertie")
plt.grid()
plt.show()

# Choisir K selon la courbe (ici on suppose que le coude est vers K=3)
K_optimal = 3

# ------------------------------
#  5. Appliquer K-Means avec le meilleur K
# ------------------------------
kmeans = KMeans(n_clusters=K_optimal, random_state=0)
df['Cluster'] = kmeans.fit_predict(X_scaled)  # ajoute le numéro de cluster à chaque ligne

print("\nClusters attribués à chaque smartphone :")
print(df)

# ------------------------------
#  6. Interpréter les groupes
# ------------------------------
centroids = scaler.inverse_transform(kmeans.cluster_centers_)
print("\nCentres de chaque cluster (valeurs moyennes réelles) :")
for i, center in enumerate(centroids):
    print(f"Cluster {i} : Prix={center[0]:.2f} DH, Autonomie={center[1]:.2f} h, Caméra={center[2]:.2f} MP")

# ------------------------------
#  7. Recommandation à l'utilisateur
# ------------------------------
prix_user = float(input("\n Entrez le prix souhaité (DH) : "))
autonomie_user = float(input(" Entrez l'autonomie souhaitée (en heures) : "))
camera_user = float(input(" Entrez la qualité de caméra souhaitée (en MP) : "))

# Transformer les données de l'utilisateur de la même manière que les smartphones
user_data = np.array([[prix_user, autonomie_user, camera_user]])
user_data_scaled = scaler.transform(user_data)

# Trouver le cluster le plus proche
user_cluster = kmeans.predict(user_data_scaled)[0]
print(f"\n Votre profil correspond le plus au cluster {user_cluster}")

# Recommander les téléphones de ce cluster
recommendations = df[df['Cluster'] == user_cluster]
print("\n Téléphones recommandés pour vous :")
print(recommendations[['Nom', 'Prix', 'Autonomie', 'Camera']])

# ------------------------------
#  8. Visualisation des clusters
# ------------------------------
plt.figure(figsize=(8, 6))

# Chaque cluster aura une couleur différente
plt.scatter(
    X_scaled[:, 0], X_scaled[:, 1],
    c=df['Cluster'], cmap='viridis', s=100, alpha=0.6, edgecolors='black'
)

# Afficher les centres des clusters
centers = kmeans.cluster_centers_
plt.scatter(
    centers[:, 0], centers[:, 1],
    c='red', s=250, marker='X', label='Centres des clusters'
    
)

# Titres et légendes
plt.title("Visualisation des clusters K-Means (Prix vs Autonomie)")
plt.xlabel("Prix (normalisé)")
plt.ylabel("Autonomie (normalisée)")
plt.legend()
plt.grid(True)
plt.show()

