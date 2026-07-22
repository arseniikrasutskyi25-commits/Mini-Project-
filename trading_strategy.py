import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    import yfinance as yf
except ImportError:
    yf = None

TICKER = "NVDA"
START_DATE = "2022-01-01"
END_DATE = "2026-07-01"
SHORT_WINDOW = 20
LONG_WINDOW = 50
INITIAL_CAPITAL = 10_000

def fetch_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    if yf is None:
        raise ImportError("Бібліотека yfinance не встановлена. Виконайте: pip install yfinance")

    print(f"Завантажуємо дані для {ticker} з {start} по {end}...")
    df = yf.download(ticker, start=start, end=end, auto_adjust=True)

    if df.empty:
        raise ValueError(
            "Дані не завантажені. Перевірте інтернет-з'єднання, "
            "правильність тікера або доступність yfinance API."
        )

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    print(f"Отримано {len(df)} торгових днів.")
    return df

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.sort_index()
    df = df.dropna(subset=["Open", "High", "Low", "Close", "Volume"])
    return df

def add_moving_averages(df: pd.DataFrame, short_window: int, long_window: int) -> pd.DataFrame:
    df = df.copy()
    df["SMA_short"] = df["Close"].rolling(window=short_window).mean()
    df["SMA_long"] = df["Close"].rolling(window=long_window).mean()
    return df
