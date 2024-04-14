import pandas as pd

cis_bdpm = pd.read_csv('CIS_bdpm.csv')
cis_cip_bdpm = pd.read_csv('CIS_CIP_bdpm.csv')
cis_has_asmr_bdpm = pd.read_csv('CIS_HAS_ASMR_bdpm.csv')
cis_has_smr_bdpm = pd.read_csv('CIS_HAS_SMR_bdpm.csv')

donnees_marketing = pd.read_csv('marketing_data.csv')


cis_bdpm = cis_bdpm.rename(columns={'Dénomination du médicament': 'Nom', 'Etat de commercialisation': 'Etat commercialisation'})
cis_cip_bdpm = cis_cip_bdpm.rename(columns={'Prix du médicament en euro': 'Prix', 'Taux de remboursement': 'Taux remboursement'})


cis_bdpm = cis_bdpm[['Code CIS', 'Nom', 'Etat commercialisation']]
cis_cip_bdpm = cis_cip_bdpm[['Code CIS', 'Prix', 'Taux remboursement']]
cis_has_asmr_bdpm = cis_has_asmr_bdpm[['Code CIS', 'Valeur de l’ASMR', 'Libellé de l’ASMR']]
cis_has_smr_bdpm = cis_has_smr_bdpm[['Code CIS', 'Valeur de l’ASMR', 'Libellé de l’ASMR']]


merged_df = pd.merge(cis_bdpm, cis_cip_bdpm, on='Code CIS', how='outer')
merged_df = pd.merge(merged_df, cis_has_asmr_bdpm, on='Code CIS', how='outer').rename(columns={'Valeur de l’ASMR': 'Valeur ASMR'})
merged_df = pd.merge(merged_df, cis_has_smr_bdpm, on='Code CIS', how='outer')


final_df = pd.merge(merged_df, donnees_marketing, on='Code CIS', how='outer')

final_df.to_csv('final_data.csv', index=False)

print(final_df.head())
