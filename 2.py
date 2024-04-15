import pandas as pd

combined_data = pd.read_csv('final_data_cleaned.csv')

def clean_remboursement(value):
    if isinstance(value, str):
        value = value.replace('%', '').strip()

        parts = value.split('.')
        if len(parts) > 2: 
            value = ''.join(parts[:-1]) + '.' + parts[-1]
        elif len(parts) == 2:
            value = value.replace('.', ',')
        
        value = value.replace(',', '.')
        
        try:
            return float(value)
        except ValueError:
            return None 
    return value

combined_data['taux_remboursement'] = combined_data['taux_remboursement'].apply(clean_remboursement)

combined_data.to_csv('final_data_cleaned.csv', index=False)