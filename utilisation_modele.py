import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
combined_data = pd.read_csv('final_data_cleaned.csv')

# Charger le modèle 
model = joblib.load('model.pkl')

# Séparation des données en variables explicatives et variable cible
X = combined_data.drop(columns=['augmentation_prescriptions'])
y = combined_data['augmentation_prescriptions']

# Utilisation du modèle pour faire des prédictions
y_pred = model.predict(X)

# Calcul de l'erreur quadratique moyenne
mse = mean_squared_error(y, y_pred)
print(f'Mean Squared Error: {mse}')

# Sauvegarde des prédictions
combined_data['augmentation_prescriptions_pred'] = y_pred
combined_data.to_csv('final_data_predictions.csv', index=False)

# Graphique des prédictions
sns.scatterplot(x='augmentation_prescriptions', y='augmentation_prescriptions_pred', data=combined_data)
plt.xlabel('Valeurs réelles')
plt.ylabel('Prédictions')
plt.title('Prédictions vs Valeurs réelles')

plt.show()