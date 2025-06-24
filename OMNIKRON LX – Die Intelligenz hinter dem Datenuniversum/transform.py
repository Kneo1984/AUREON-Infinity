import pandas as pd

def clean_data(df):
    """
    Führt grundlegende Datenbereinigung durch:
    - Entfernt leere Zeilen
    - Entfernt Duplikate
    - Entfernt führende/nachgestellte Leerzeichen in Strings
    """
    df = df.dropna(how="all")
    df = df.drop_duplicates()

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)

    print("[INFO] Datenbereinigung abgeschlossen.")
    return df

# Optionaler Testlauf im Terminal
if __name__ == "__main__":
    import os
    df = pd.read_csv("beispiel.csv")
    df_cleaned = clean_data(df)
    print(df_cleaned)

