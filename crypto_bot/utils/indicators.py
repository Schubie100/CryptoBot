import pandas as pd

def add_sma(data, window, column="close"):
    """
    Add Simple Moving Average (SMA) to the data.
    """
    data[f"SMA{window}"] = data[column].rolling(window=window).mean()
    return data

def add_indicators(data):
    """
    Add multiple technical indicators to the dataset.
    """
    data = add_sma(data, 50)   # Add SMA50
    data = add_sma(data, 200)  # Add SMA200
    return data
