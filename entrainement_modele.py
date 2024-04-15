import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import joblib

# Charger les données
combined_data = pd.read_csv('final_data_cleaned.csv')

# Suppression des colonnes non nécessaires
columns_to_drop = ['nom', 'libelle_ASMR_x', 'libelle_ASMR_y', 'valeur_ASMR', 'canaux_diffusion', 'date_lancement', 'duree_campagne']
combined_data.drop(columns=columns_to_drop, inplace=True)

# Exclusion des lignes dont les colonnes sont vide
combined_data.dropna(subset=['prix'], inplace=True)
combined_data.dropna(subset=['budget_marketing_total'], inplace=True)
combined_data.dropna(subset=['augmentation_prescriptions'], inplace=True)
combined_data.dropna(subset=['augmentation_ventes'], inplace=True)

# Séparation des données en variables explicatives et variable cible
X = combined_data.drop(columns=['augmentation_prescriptions'])
y = combined_data['augmentation_prescriptions']

# Séparation des données en données d'entraînement et données de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Création du pipeline
numeric_features = ['prix', 'budget_marketing_total', 'taux_remboursement']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features)
])

# Réglage hyperparametre via grid search
param_grid = {
    'regressor__n_estimators': [100, 200, 300],
    'regressor__max_features': ['sqrt', 'log2', None],
    'regressor__max_depth': [None, 10, 20, 30],
    'regressor__min_samples_split': [2, 5, 10]
}


# Création du modèle
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor())
])

# Création de l'objet GridSearchCV
search = GridSearchCV(model, param_grid, cv=5, scoring='neg_mean_squared_error', verbose=3)

# Exécution de la recherche
search.fit(X_train, y_train)
print("Meilleurs paramètres:", search.best_params_)
print("Meilleur score MSE:", -search.best_score_)

# Entraînement du modèle
model.fit(X_train, y_train)

# Prédiction
y_pred = model.predict(X_test)

# Evaluation du modèle
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Sauvegarde du modèle
joblib.dump(model, 'model.pkl')