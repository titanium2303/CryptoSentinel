from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from analysis import analyze_market
from config import TELEGRAM_BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 CryptoSentinel is active and watching BTC!")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    action, confidence, reasons = analyze_market()
    text = f"[BTC/USDT]\nSuggested Action: {action} ({confidence:.1f}%)\nReasons:\n"
    text += "\n".join(f"- {r}" for r in reasons)
    await update.message.reply_text(text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - Activate bot\n/status - Get current recommendation\n/help - Commands")

def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()
