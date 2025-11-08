import pandas as pd
import os
import logging

def extract_data(file_path: str, data_type: str = "data") -> pd.DataFrame:
    try:
        abs_path = os.path.join(os.path.dirname(__file__), '..', file_path)
        df = pd.read_csv(abs_path)
        logging.info(f"{data_type.capitalize()} data extracted: {len(df)} rows.")
        return df
    except Exception as e:
        logging.error(f"Error extracting {data_type}: {e}")
        return pd.DataFrame()
