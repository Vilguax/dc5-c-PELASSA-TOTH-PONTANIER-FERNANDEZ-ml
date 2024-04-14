import pandas as pd
import numpy as np

cis_bdpm = pd.read_csv('CIS_bdpm.csv')
cis_cip_bdpm = pd.read_csv('CIS_CIP_bdpm.csv')
cis_has_asmr_bdpm = pd.read_csv('CIS_HAS_ASMR_bdpm.csv')
cis_has_smr_bdpm = pd.read_csv('CIS_HAS_SMR_bdpm.csv')


code_cis = cis_bdpm['Code CIS'].tolist() + cis_cip_bdpm['Code CIS'].tolist() + cis_has_asmr_bdpm['Code CIS'].tolist() + cis_has_smr_bdpm['Code CIS'].tolist()
code_cis = list(set(code_cis))


np.random.seed(492031283)

n_campaigns = len(code_cis)

all_possible_dates = pd.date_range(start="2009-01-01", end="2024-03-28", freq='D')

random_launch_dates = np.random.choice(all_possible_dates, size=n_campaigns)

data = {
    "Code CIS": np.random.choice(code_cis, n_campaigns, replace=False),
    "Budget Marketing Total": np.random.randint(5000, 50000, n_campaigns),
    "Canaux de Diffusion": np.random.choice(["Réseaux Sociaux", "Télévision", "Radio", "Presse", "Internet"], n_campaigns),
    "Cible Démographique": np.random.choice(["18-24 ans", "25-34 ans", "35-44 ans", "45-54 ans", "55-64 ans", "65 ans et plus"], n_campaigns),
    "Date de Lancement": random_launch_dates,  # Utilisez les dates de lancement aléatoires ici
    "Durée de la Campagne (jours)": np.random.randint(30, 180, n_campaigns),
    "Augmentation Observée des Prescriptions (%)": np.random.uniform(5, 20, n_campaigns).round(2),
    "Augmentation Observée des Ventes (%)": np.random.uniform(5, 25, n_campaigns).round(2)
}

marketing_data = pd.DataFrame(data)
marketing_data.to_csv("marketing_data.csv", index=False)

marketing_data.head()
