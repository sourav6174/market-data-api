import yfinance as yf

def fetch_nifty():
    ticker = yf.Ticker("^NSEI")
    
    try:
        info = ticker.fast_info
        current_price = float(info["last_price"])
        prev_close = float(info["previous_close"])
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
        prev_close = float(info["previous_close"])
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
