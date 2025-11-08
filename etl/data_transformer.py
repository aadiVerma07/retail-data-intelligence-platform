import pandas as pd
import logging
def get_city_revenue(customer_data,order_data):
    """Transforms and aggregates data to calculate total revenue per city."""
    try:
        # Merge customer and order data on 'customer_id'
        merged_data=pd.merge(order_data,customer_data,on='customer_id',how='inner')
        # Group by 'city' and sum 'order_amount' to get total revenue per cit
        city_revenue=merged_data.groupby('city')['amount'].sum().reset_index().rename(columns={"amount":"total_revenue"})
        city_revenue=city_revenue.sort_values(by=["city","total_revenue"],ascending=[True,False])
        logging.info("City-level revenue transformation completed.")
        return city_revenue
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        return pd.DataFrame()
def get_top_categories(customers, orders):
    """Transform data to find top 5 categories per city."""
    try:
        # Merge orders and customers on 'customer_id'
        merged_data = pd.merge(orders, customers, on='customer_id', how='inner')
        # Group by 'category' and sum 'amount' to get total revenue per category
        category_summary = merged_data.groupby(["city","category"])['amount'].sum().reset_index().rename(columns={"amount": "total_revenue"})
        category_summary['rank']=category_summary.groupby(['city'])['total_revenue'].rank(method='first', ascending=False)
        top5=category_summary[category_summary['rank'] <=5]
        logging.info("Category-level transformation completed.")
        return top5.sort_values(by=["city","rank"]).reset_index(drop=True)
    except Exception as e:
        logging.error(f"Error during category transformation: {e}")
        return pd.DataFrame()
def get_transform_detailed_orders(orders, customers):
    """Join and enrich order data with customer info."""
    try:
        merged = pd.merge(orders, customers, on="customer_id", how="left")
        merged = merged[["order_id", "customer_id", "city", "category",
                        "payment_method", "amount", "date"]]
        logging.info("Orders enriched with customer city info.")
        return merged
    except Exception as e:
        logging
        return pd.DataFrame()