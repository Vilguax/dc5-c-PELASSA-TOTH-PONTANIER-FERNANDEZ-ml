import pandas as pd
import numpy as np

np.random.seed(492031283)

n_campaigns = 300
data = {
    "Code CIS": np.random.randint(100000, 999999, n_campaigns),
    "Budget Marketing Total": np.random.randint(5000, 50000, n_campaigns),
    "Canaux de Diffusion": np.random.choice(["Réseaux Sociaux", "Télévision", "Radio", "Presse", "Internet"], n_campaigns),
    "Cible Démographique": np.random.choice(["18-24 ans", "25-34 ans", "35-44 ans", "45-54 ans", "55-64 ans", "65 ans et plus"], n_campaigns),
    "Date de Lancement": pd.date_range(start="2022-01-01", periods=n_campaigns, freq='M'),
    "Durée de la Campagne (jours)": np.random.randint(30, 180, n_campaigns),
    "Augmentation Observée des Prescriptions (%)": np.random.uniform(5, 20, n_campaigns).round(2),
    "Augmentation Observée des Ventes (%)": np.random.uniform(5, 25, n_campaigns).round(2)
}

marketing_data = pd.DataFrame(data)

marketing_data.to_csv("marketing_data.csv", index=False)

marketing_data.head()