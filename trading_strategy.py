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

