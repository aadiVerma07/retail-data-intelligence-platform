from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Flipkart Data Intelligence API")
app.include_router(router)

@app.get("/")
def home():
    return { "message": "Welcome to Flipkart Analytics API",
        "endpoints": [
            "/api/cities",
            "/api/top_cities",
            "/api/categories/{city}"
        ]}
