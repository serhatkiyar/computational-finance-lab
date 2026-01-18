import pandas as pd
import numpy as np

def validate_ols_input(df, target_col, feature_cols):
    
    # 1. Tip Kontrolü
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Veri seti pandas DataFrame olmalıdır.")
    
    # 2. Sütun Kontrolü
    required_cols = [target_col] + feature_cols
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        raise ValueError(f"Eksik sütunlar: {missing_cols}")

    # Analiz edilecek alt kümeyi al
    subset = df[required_cols]

    # 3. NaN (Boş Veri) Kontrolü
    if subset.isnull().values.any():
        raise ValueError("Veri setinde NaN değerler var.")

    # 4. Sonsuz (Inf) Kontrolü
    if np.isinf(subset).values.any():
         raise ValueError("Veri setinde sonsuz (inf) değerler var.")

    return True