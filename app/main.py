from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.scraper import (
    fetch_nifty,
    fetch_sensex,
    fetch_sector_heatmap,
    fetch_india_vix,
    fetch_usd_inr,
    fetch_crude_oil,
    fetch_gold,
    fetch_world_indices
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
        vix = get_cached("vix", fetch_india_vix)
        usd_inr = get_cached("usd_inr", fetch_usd_inr)
        crude = get_cached("crude", fetch_crude_oil)
        gold = get_cached("gold", fetch_gold)
        world_indices = get_cached("world_indices", fetch_world_indices)

        return {
            "nifty": nifty,
            "sensex": sensex,
            "heatmap": heatmap,
            "india_vix": vix,
            "global_assets": {
                "usd_inr": usd_inr,
                "crude_oil": crude,
                "gold": gold
            },
            "world_indices": world_indices
        }

    except Exception as e:
        return {"error": str(e)}