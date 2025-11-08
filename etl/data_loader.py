import sqlite3
import logging
import os

def load_to_db(df, table_name):
    try:
        db_path = os.path.join(os.path.dirname(__file__), '..', 'data\processed', 'etl_project.db')
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        logging.info(f"Loaded {len(df)} rows into '{table_name}'.")
    except Exception as e:
        logging.error(f"Failed to load {table_name}: {e}")
