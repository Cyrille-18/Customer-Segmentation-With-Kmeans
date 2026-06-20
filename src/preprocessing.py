import pandas as pd

def load_data(path: str):
    return pd.read_csv(path)

def assess_quality(df):
    return {
        'rows': df.shape[0],
        'columns': df.shape[1],
        'missing_values': int(df.isnull().sum().sum()),
        'duplicates': int(df.duplicated().sum())
    }

def clean_data(df):
    df = df.copy()
    df.dropna(inplace=True)
    df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], dayfirst=True)
    return df