import pandas as pd

combined_data = pd.read_csv('final_data_cleaned.csv')

def delete_empty_collumns():
    columns_to_drop = ['prix', 'budget_marketing_total', 'augmentation_prescriptions', 'augmentation_ventes']
    combined_data.drop(columns=columns_to_drop, inplace=True)
    return combined_data

combined_data.to_csv('final_data_cleaned.csv', index=False)