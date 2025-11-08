from etl.data_extractor import extract_data
from etl.data_transformer import get_city_revenue, get_top_categories,get_transform_detailed_orders
from etl.data_loader import load_to_db
from etl.utils import setup_logger
import logging

def run_etl():
    try:
        logger = setup_logger()
        logger.info("Starting Flipkart ETL Pipeline...")
        orders = extract_data("data/raw/orders.csv", "orders")
        customers = extract_data("data/raw/customers.csv", "customers")

        if orders.empty or customers.empty:
            logging.error("Missing raw data.")
            return

        city_revenue = get_city_revenue(customers,orders)
        top_categories = get_top_categories(customers,orders)
        orderdetails = get_transform_detailed_orders(orders,customers)
        load_to_db(city_revenue, "city_revenue")
        load_to_db(top_categories, "top_categories")
        load_to_db(orderdetails, "detailed_orders")
        logging.info("ETL Pipeline completed successfully.")
    except Exception as e:
        logging.error(f"ETL process failed: {e}")

if __name__ == "__main__":
    run_etl()
