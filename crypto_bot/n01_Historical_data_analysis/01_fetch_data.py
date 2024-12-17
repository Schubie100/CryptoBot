# 01_fetch_data.py - Auto-generated
import ccxt
import pandas as pd
from datetime import datetime
import os

# === Configurations ===
SYMBOLS = [
    "BTC/USDT",  # Bitcoin
    "ETH/USDT",  # Ethereum
    "LTC/USDT",  # Litecoin
    "ADA/USDT",  # Cardano
    "SOL/USDT",  # Solana
    "VET/USDT",  # VeChain
    "ONE/USDT",  # Harmony
]
TIMEFRAME = '1h'  # Hourly data
START_DATE = '2018-01-01T00:00:00Z'  # Start date for fetching data
OUTPUT_FOLDER = "data"  # Folder to store fetched data

# === Fetch Data Function ===
def fetch_data(exchange, symbol, start_date, timeframe='1h', limit=1000):
    """
    Fetches historical OHLCV data incrementally for a given symbol.
    Returns the data as a pandas DataFrame.
    """
    all_data = []
    since = exchange.parse8601(start_date)  # Convert start date to timestamp

    while True:
        try:
            # Fetch OHLCV data
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=since, limit=limit)
            if not ohlcv:
                break  # Stop when no more data is returned

            # Append data
            all_data.extend(ohlcv)
            since = ohlcv[-1][0] + 1  # Update the timestamp to fetch next batch

            # Print progress
            print(f"Fetched {len(all_data)} rows for {symbol}...")
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            break

    # Convert to DataFrame
    df = pd.DataFrame(all_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# === Main Script ===
if __name__ == "__main__":
    # Initialize Binance.US exchange
    exchange = ccxt.binanceus()

    # Create output folder if it doesn't exist
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Fetch data for each symbol
    for symbol in SYMBOLS:
        print(f"\nFetching data for {symbol}...")
        try:
            # Fetch historical data
            data = fetch_data(exchange, symbol, START_DATE, TIMEFRAME)

            # Save to CSV
            pair = symbol.replace("/", "_")
            file_path = os.path.join(OUTPUT_FOLDER, f"{pair}_{TIMEFRAME}.csv")
            data.to_csv(file_path, index=False)
            print(f"Data for {symbol} saved to {file_path}")
        except Exception as e:
            print(f"Failed to fetch data for {symbol}: {e}")
