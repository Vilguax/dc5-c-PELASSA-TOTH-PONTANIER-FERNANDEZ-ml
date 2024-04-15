import pandas as pd

combined_data = pd.read_csv('final_data.csv')

def clean_currency(value):
    """Nettoie et convertit les prix en float."""
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

combined_data['Prix'] = combined_data['Prix'].apply(clean_currency)