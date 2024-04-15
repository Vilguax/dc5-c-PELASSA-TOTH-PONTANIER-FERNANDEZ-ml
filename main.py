import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Charger les données
combined_data = pd.read_csv('final_data_cleaned.csv')

# Fonction pour nettoyer et convertir les colonnes de prix et de taux de remboursement
def clean_currency(value):
    """Convertit les valeurs monétaires en float."""
    if isinstance(value, str):
        value = value.replace('%', '').replace(',', '.').strip()
        return float(value)
    return value

# Nettoyage des données
combined_data['prix'] = combined_data['prix'].apply(clean_currency)
combined_data['taux_remboursement'] = combined_data['taux_remboursement'].apply(lambda x: float(x.strip('%'))/100 if isinstance(x, str) else x)

# Suppression des colonnes non nécessaires
columns_to_drop = ['nom', 'libelle_ASMR_x', 'libelle_ASMR_y', 'valeur_ASMR', 'canaux_diffusion', 'date_lancement', 'duree_campagne', 'augmentation_ventes']
combined_data.drop(columns=columns_to_drop, inplace=True)

# Imputation des valeurs manquantes
numeric_features = combined_data.select_dtypes(include=['float64', 'int64']).columns.tolist()
categorical_features = combined_data.select_dtypes(include=['object']).columns.tolist()

numeric_imputer = SimpleImputer(strategy='median')
categorical_imputer = SimpleImputer(strategy='most_frequent')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_imputer, numeric_features),
        ('cat', categorical_imputer, categorical_features)
    ],
    remainder='passthrough'
)

# Préparation des données pour l'entraînement
y = combined_data['augmentation_prescriptions']
X = combined_data.drop('augmentation_prescriptions', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construction du pipeline de machine learning
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Entraînement du modèle
pipeline.fit(X_train, y_train)

# Prédiction sur les données de test et calcul de l'erreur
y_pred = pipeline.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f'RMSE: {rmse}')
