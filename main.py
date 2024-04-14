import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

combined_data = pd.read_csv('final_data.csv')

combined_data['Prix'] = combined_data['Prix'].apply(lambda x: float(x.replace(',', '.').replace('%', '')) if isinstance(x, str) else x)
combined_data['Taux remboursement'] = combined_data['Taux remboursement'].apply(lambda x: float(x.strip('%'))/100 if isinstance(x, str) else x)

columns_to_drop = ['Nom', 'Libellé de l’ASMR_x', 'Libellé de l’ASMR_y', 'Valeur de l’ASMR', 'Canaux de Diffusion', 'Date de Lancement', 'Durée de la Campagne (jours)', 'Augmentation Observée des Ventes (%)']
combined_data.drop(columns=columns_to_drop, inplace=True)

numeric_features = combined_data.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = combined_data.select_dtypes(include=['object']).columns.difference(numeric_features)

numeric_imputer = SimpleImputer(strategy='median')
categorical_imputer = SimpleImputer(strategy='most_frequent')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_imputer, numeric_features),
        ('cat', categorical_imputer, categorical_features)
    ],
    remainder='passthrough')

if 'Augmentation Observée des Prescriptions (%)' in combined_data.columns:
    y = combined_data['Augmentation Observée des Prescriptions (%)']
    X = combined_data.drop(['Augmentation Observée des Prescriptions (%)'], axis=1)
else:
    raise Exception("Column 'Augmentation Observée des Prescriptions (%)' not found in DataFrame.")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f'RMSE: {rmse}')