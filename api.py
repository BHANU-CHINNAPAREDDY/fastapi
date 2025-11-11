from fastapi import FastAPI
from fastapi.responses import JSONResponse
from db import DatabaseConnection

app = FastAPI()

db = DatabaseConnection()

@app.get("/")
def home():
    return "Welcome to metal prices api"

@app.get("/gold-prices")
def get_gold_prices():
    records = db.get_all_gold_records()
    if not records:
        return JSONResponse(content={"success": False, "message": "No records found"}, status_code=404)
    
    data = [
        {
            "id": r.id,
            "country": r.country,
            "city": r.city,
            "currency": r.currency,
            "gold_24k": r.gold_24k,
            "gold_22k": r.gold_22k,
            "gold_18k": r.gold_18k,
            "gold_24k_inr": r.gold_24k_inr,
            "gold_22k_inr": r.gold_22k_inr,
            "gold_18k_inr": r.gold_18k_inr,
            "date_scraped": r.date_scraped
        }
        for r in records
    ]
    return JSONResponse(content={"success": True, "data": data}, status_code=200)

@app.get("/silver-platinum-prices")
def get_silver_platinum_prices():
    records = db.get_all_silver_and_platinum_records()
    if not records:
        return JSONResponse(content={"success": False, "message": "No records found"}, status_code=404)
    data = [
        {
            "id": r.id,
            "country": r.country,
            "city": r.city,
            "currency": r.currency,
            "silver_10gm_price": r.silver_10gm_price,
            "platinum_10gm_price": r.platinum_10gm_price,
            "date_scraped": r.date_scraped

        }
        for r in records
    ]
    return JSONResponse(content={"success": True, "data": data})