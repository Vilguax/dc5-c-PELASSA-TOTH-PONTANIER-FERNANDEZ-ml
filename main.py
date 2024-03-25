import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Chargement des datasets
clients = pd.read_csv('dataset_clients.csv')
marketing = pd.read_csv('dataset_marketing_grand.csv')

# Entrainement du modèle
X = clients[['Âge']]
Y = clients['Indice Satisfaction']

# Split des données
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Création du modèle
model = LinearRegression()
model.fit(X_train, Y_train)

# Prédiction
Y_pred = model.predict(X_test)

# Visualisation des résultats
plt.scatter(X_test['Âge'], Y_test, color='red')
plt.scatter(X_test['Âge'], Y_pred, color='blue')
plt.title('Âge vs Indice Satisfaction')
plt.xlabel('Âge')
plt.ylabel('Indice Satisfaction')
plt.show()