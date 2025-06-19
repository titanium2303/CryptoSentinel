# 📊 CryptoSentinel

**CryptoSentinel** is a Telegram bot that automatically analyzes the Bitcoin (BTC/USDT) market every 15 minutes using multiple technical indicators and provides BUY / SELL / HOLD signals with a confidence percentage.

---

## 🚀 Features

- 🔄 Analyzes BTC/USDT every 15 minutes (customizable)
- 📈 Uses indicators: RSI, MACD, EMA Crossover, Bollinger Bands
- 📊 Calculates signal confidence (0–100%)
- ⚠️ Alerts when confidence >80% immediately
- ⏱ Notifies if confidence >70% persists for 1 hour
- 💬 Responds to `/status` and `/help` commands
- 🧠 Minimal configuration, no trading knowledge required
- 🗃️ SQLite database to store recent signals
- 📝 Logs activities and errors to `bot.log` and `errors.log`

---

## 📦 Requirements

- Python 3.10+
- Telegram bot token (create via [@BotFather](https://t.me/BotFather))
- Your Telegram User ID (get it via [@userinfobot](https://t.me/userinfobot))

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/cryptosentinel.git
cd cryptosentinel
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your bot

Edit config.py:

```python
TELEGRAM_BOT_TOKEN = "your_bot_token_here"
```

Edit main.py and replace:

```python
YOUR_CHAT_ID = 123456789  # Replace with your Telegram ID
```

▶️ Run the bot

```bash
python main.py
```

The bot will begin monitoring BTC and send you actionable alerts when signals are strong.

## 📡 Available Commands
Command	Description
/start	Activate the bot
/status	Get current market analysis
/help	Show available commands

## 📁 Project Structure

btc_bot/
├── analysis.py       # Market analysis and indicators
├── bot.py            # Telegram bot commands
├── config.py         # Settings and thresholds
├── db.py             # SQLite signal storage
├── logger.py         # Logging setup
├── main.py           # App entry point
├── requirements.txt  # Python dependencies
└── README.md         # This file

## 📒 Sample Signal Output

[BTC/USDT]
## 🚨 Action: Buy (87.3%)
Reasons:
- RSI indicates oversold
- MACD indicates upward momentum
- EMA crossover indicates uptrend
- High volatility detected

## 🧩 To-Do / Future Features

    ✅ Basic logging and analysis

    🔄 Multi-timeframe support

    📤 Email or SMS notifications

    📈 Signal visualization dashboard

    🧠 Machine learning-based signal confidence

## 📜 License

MIT License. Use freely and responsibly.
