import yfinance as yf

def fetch_nifty():
    ticker = yf.Ticker("^NSEI")
    
    try:
        info = ticker.fast_info
        current_price = float(info["last_price"])
        # prev_close = float(info["previous_close"])

        new_data = ticker.history(period="5d")
        prev_close = float(new_data["Close"].iloc[-2])

    except Exception:
        data = ticker.history(period="5d")
        if len(data) < 2:
            return "NIFTY data not available"
        current_price = float(data["Close"].iloc[-1])
        prev_close = float(data["Close"].iloc[-2])

    hist = ticker.history(period="1d")
    if hist.empty:
        return "NIFTY OHLC not available"
    
    ohlc = hist.iloc[-1]

    change = current_price - prev_close
    percent = (change / prev_close) * 100

    return {
        "price": round(current_price, 2),
        "change": round(change, 2),
        "percent_change": round(percent, 2),
        "ohlc": {
            "open": round(float(ohlc["Open"]), 2),
            "high": round(float(ohlc["High"]), 2),
            "low": round(float(ohlc["Low"]), 2),
            "close": round(float(ohlc["Close"]), 2)
        }
    }

def fetch_sensex():
    ticker = yf.Ticker("^BSESN")
    
    try:
        info = ticker.fast_info
        current_price = float(info["last_price"])
        # prev_close = float(info["previous_close"])

        new_data = ticker.history(period="5d")
        prev_close = float(new_data["Close"].iloc[-2])

    except Exception:
        data = ticker.history(period="5d")
        if len(data) < 2:
            return "SENSEX data not available"
        current_price = float(data["Close"].iloc[-1])
        prev_close = float(data["Close"].iloc[-2])

    hist = ticker.history(period="1d")
    if hist.empty:
        return "SENSEX OHLC not available"
    
    ohlc = hist.iloc[-1]

    change = current_price - prev_close
    percent = (change / prev_close) * 100

    return {
        "price": round(current_price, 2),
        "change": round(change, 2),
        "percent_change": round(percent, 2),
        "ohlc": {
            "open": round(float(ohlc["Open"]), 2),
            "high": round(float(ohlc["High"]), 2),
            "low": round(float(ohlc["Low"]), 2),
            "close": round(float(ohlc["Close"]), 2)
        }
    }

# Sector Tickers

SECTOR_STOCKS = {

    "banking": [
        "HDFCBANK.NS",
        "ICICIBANK.NS",
        "SBIN.NS"
    ],
    "it": [
        "TCS.NS",
        "INFY.NS",
        "WIPRO.NS"
    ],
    "pharma": [
        "SUNPHARMA.NS",
        "CIPLA.NS",
        "DRREDDY.NS"
    ],
    "fmcg": [
        "HINDUNILVR.NS",
        "ITC.NS",
        "NESTLEIND.NS"
    ],
    "auto": [
        "MARUTI.NS",
        "TATAMOTORS.NS",
        "M&M.NS"
    ],
    "energy_oil_gas": [
        "RELIANCE.NS",
        "ONGC.NS",
        "BPCL.NS"
    ],
    "metals_mining": [
        "TATASTEEL.NS",
        "HINDALCO.NS",
        "JSWSTEEL.NS"
    ],
    "infra_real_estate": [
        "LT.NS",
        "DLF.NS",
        "GODREJPROP.NS"
    ]
}

def fetch_sector_data(sector_name, stocks):

    changes = []

    for stock_symbol in stocks:
        try:
            ticker = yf.Ticker(stock_symbol)
            info = ticker.fast_info
            current_price = float(info["last_price"])
            prev_close = float(info["previous_close"])
            percent_change = (
                (current_price - prev_close) / prev_close
            ) * 100
            changes.append(percent_change)

        except Exception:
            continue

    if not changes:
        return {
            "sector": sector_name,
            "error": "Data unavailable"
        }

    avg_change = sum(changes) / len(changes)

    if avg_change > 0:
        sentiment = "bullish"
        color = "green"
    elif avg_change < 0:
        sentiment = "bearish"
        color = "red"
    else:
        sentiment = "neutral"
        color = "gray"

    return {
        "sector": sector_name,
        "percent_change": round(avg_change, 2),
        "sentiment": sentiment,
        "color": color
    }

def fetch_sector_heatmap():
    heatmap = {}
    for sector_name, stocks in SECTOR_STOCKS.items():
        heatmap[sector_name] = fetch_sector_data(
            sector_name,
            stocks
        )
    return heatmap