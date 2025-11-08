from fastapi import APIRouter, Query
from api.db_service import fetch_top_cities, fetch_city_categories, fetch_cities,get_city_revenue_payment_summary,get_payment_summary
from datetime import datetime

router = APIRouter(prefix="/api")

@router.get("/cities")
def get_cities():
    return fetch_cities()

@router.get("/top_cities")
def get_top_cities(limit: int =Query(0,description="Number of top cities to fetch")):
    return fetch_top_cities(limit)

@router.get("/categories/{city}")
def get_city_categories(
    city: str,
    start_date: str = Query("2023-01-01"),
    end_date: str = Query(datetime.now().strftime("%Y-%m-%d"))
):
    return fetch_city_categories(city, start_date, end_date)
@router.get("/total_city")
def get_total_city():
    return get_city_revenue_payment_summary()
@router.get("/payment_summary")
def get_payment_details():
    return get_payment_summary()
