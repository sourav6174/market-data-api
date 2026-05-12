from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.scraper import (
    fetch_nifty,
    fetch_sensex,
    fetch_sector_heatmap
)
from app.cache import get_cached

app = FastAPI()

# Allow your extension to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict later
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/market-data")
def market_data():
    try:
        nifty = get_cached("nifty", fetch_nifty)
        sensex = get_cached("sensex", fetch_sensex)
        heatmap = get_cached("heatmap", fetch_sector_heatmap)

        return {
            "nifty": nifty,
            "sensex": sensex,
            "heatmap": heatmap
        }

    except Exception as e:
        return {"error": str(e)}