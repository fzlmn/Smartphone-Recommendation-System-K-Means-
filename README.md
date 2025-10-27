# 📱 Smartphone Recommendation System (K-Means)
## 🧠 Description

This project is a simple recommendation system that suggests smartphones to users based on their preferences for price, battery life (autonomy), and camera quality.

It uses the K-Means clustering algorithm to group similar smartphones into clusters.
When a user enters their preferences, the system finds which cluster best matches those preferences and recommends phones from that same group.

## ⚙️ How It Works (Concept)

📊 The program reads an Excel file (smartphones.xlsx) containing smartphones and their features:

Price (DH)

Autonomy (in hours)

Camera (in megapixels)

🧩 The data is normalized so all features have equal importance.

🔍 The K-Means algorithm groups similar phones together (ex: budget phones, mid-range phones, and premium phones).

🧭 The “elbow method” is used to find the best number of clusters (K).

👤 The user enters their desired price, autonomy, and camera.

📱 The program finds the cluster closest to those preferences and recommends phones from that group.

## 🧰 Technologies Used

Python 3

pandas

numpy

matplotlib

scikit-learn

## 📂 Project Structure
📁 Smartphone-Recommendation/

│

├── smartphones.xlsx         # Dataset

├── K-means.py    # Main Python script

└── README.md                # Project documentation

## ▶️ How to Run the Program
### 1. Install the dependencies

Open your terminal and run:

pip install pandas numpy matplotlib scikit-learn openpyxl


(The openpyxl library is needed to read Excel files.)

### 2. Run the Python script

Make sure your Excel file is in the same folder as your .py script,
then run:

python k-means.py

### 3. Follow the steps in the terminal

You’ll be asked to enter:

your desired price

autonomy (battery life)

and camera quality

Example:

 Entrez le prix souhaité (DH) : 4000
 Entrez l'autonomie souhaitée (en heures) : 15
 Entrez la qualité de caméra souhaitée (en MP) : 48


Then, the program will display:

the smartphones grouped by cluster

the average values of each cluster

your recommended smartphones

a visual graph of the clusters.

## 📊 Example Output

### 🟢 Clusters found:

Cluster 0 : Budget phones (low price, low camera)
Cluster 1 : Mid-range phones (balanced)
Cluster 2 : High-end phones (high price, excellent specs)


### 🟢 Recommendation example:

Votre profil correspond le plus au cluster 1

Téléphones recommandés pour vous :
      Nom             Prix  Autonomie  Camera
----------------------------------------------

Xiaomi Redmi 12       1600    15         48

Infinix Note 30       2200    17         64

Oppo A78              2800    16         48

## 📈 Screenshots

1️⃣ Elbow Method Graph (Méthode du coude)

2️⃣ Cluster Visualization (Prix vs Autonomie)

3️⃣ Console Output (User input + recommendations)

Example:

<img width="700" height="380" alt="image" src="https://github.com/user-attachments/assets/9630af43-3a04-404d-9aee-e5696722da36" />

-----------------------

<img width="600" height="90" alt="image" src="https://github.com/user-attachments/assets/410d488e-5ae1-4800-aeec-4f73630a564f" />

-----------------------

<img width="700" height="380" alt="image" src="https://github.com/user-attachments/assets/3876daf6-95d4-4bd4-b87a-42ba943a9fea" />


## 🧩 What I Learned

How to use K-Means to find patterns in data.

How to build a basic recommendation system without labels.

How to visualize clusters and interpret them.
