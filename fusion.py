import pandas as pd
import os
from datetime import datetime

def standardize_date(date_str):
    for fmt in ("%m/%d/%Y %H:%M:%S", "%d/%m/%Y %H:%M:%S"):
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
    raise ValueError(f"Format '{date_str}' n'est pas supporté.")

def normalize_decimal_separator(value):
    if isinstance(value, str):
        return value.replace(',', '.')
    return value

path = "Data set csv"

files = os.listdir(path)

all_data = []

for file in files:
    if file.endswith('.csv'):
        data = pd.read_csv(f"{path}/{file}", encoding='ISO-8859-1')
        
        data['Date'] = data['Date'].apply(standardize_date)
        data['Close'] = data['Close'].apply(normalize_decimal_separator).astype(float)
        
        column_name = file.split(".")[0]
        data.rename(columns={'Close': column_name}, inplace=True)
        
        all_data.append(data)

from functools import reduce
df_merged = reduce(lambda left, right: pd.merge(left, right, on='Date', how='outer'), all_data)
df_merged.sort_values('Date', inplace=True)

for column in df_merged.columns[1:]:
    first_non_zero_index = df_merged[column].ne(0).idxmax()
    df_merged[column] = df_merged[column].fillna(0)
    df_merged.loc[first_non_zero_index:, column] = df_merged.loc[first_non_zero_index:, column].replace(0, method='ffill')

df_merged.to_csv("dataset.csv", index=False)

print("Fusion terminée.")