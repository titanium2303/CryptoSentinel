import ccxt
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator, MACD
from ta.volatility import BollingerBands
from config import SYMBOL

exchange = ccxt.binance()

def fetch_ohlcv(symbol=SYMBOL, timeframe='15m', limit=100):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df

def analyze_market():
    df = fetch_ohlcv()
    close = df['close']

    rsi = RSIIndicator(close, window=14).rsi().iloc[-1]
    macd = MACD(close).macd_diff().iloc[-1]
    ema_fast = EMAIndicator(close, window=9).ema_indicator().iloc[-1]
    ema_slow = EMAIndicator(close, window=21).ema_indicator().iloc[-1]
    bb = BollingerBands(close).bollinger_hband().iloc[-1] - BollingerBands(close).bollinger_lband().iloc[-1]

    score = 0
    reasons = []

    if rsi < 30:
        score += 25
        reasons.append("RSI indicates oversold")
    elif rsi > 70:
        score -= 25
        reasons.append("RSI indicates overbought")

    if macd > 0:
        score += 20
        reasons.append("MACD indicates upward momentum")
    elif macd < 0:
        score -= 20
        reasons.append("MACD indicates downward momentum")

    if ema_fast > ema_slow:
        score += 15
        reasons.append("EMA crossover indicates uptrend")
    else:
        score -= 15
        reasons.append("EMA crossover indicates downtrend")

    if bb > 200:
        score += 10
        reasons.append("High volatility detected")

    if score > 30:
        return "Buy", min(score, 100), reasons
    elif score < -30:
        return "Sell", min(abs(score), 100), reasons
    else:
        return "Hold", 50, reasons
