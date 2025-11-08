import sqlite3, os
import pandas as pd

def get_connection():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'data\processed', 'etl_project.db')
    return sqlite3.connect(db_path)

def fetch_top_cities(limit=10):
    conn = get_connection()
    df = pd.read_sql(f"SELECT city, total_revenue FROM city_revenue ORDER BY total_revenue DESC LIMIT {limit}", conn)
    conn.close()
    return df.to_dict(orient="records")

def fetch_city_categories(city, start_date, end_date):
    conn = get_connection()
    query = f"""
        SELECT city, category, total_revenue FROM top_categories
        WHERE city='{city}' ORDER BY total_revenue DESC LIMIT 5;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df.to_dict(orient="records")

def fetch_cities():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM city_revenue ORDER BY total_revenue DESC", conn)
    conn.close()
    return df.to_dict(orient="records")
def get_city_revenue_payment_summary():
    conn = get_connection()
    df = pd.read_sql( "SELECT COUNT(DISTINCT city) AS total_cities,SUM(amount) AS total_revenue,COUNT(DISTINCT payment_method) AS total_payment_options FROM detailed_orders", conn)
    conn.close()
    return df.to_dict(orient="records")
def get_payment_summary():
    conn = get_connection()
    df = pd.read_sql( "SELECT payment_method, SUM(amount) AS total_amount FROM detailed_orders GROUP BY payment_method ORDER BY total_amount DESC", conn)
    conn.close()
    return df.to_dict(orient="records")
    
