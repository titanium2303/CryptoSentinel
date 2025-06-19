from bot import start_bot
from analysis import analyze_market
from db import init_db, save_signal, get_recent_signals
from config import *
from logger import setup_logger
from apscheduler.schedulers.background import BackgroundScheduler
import asyncio
import logging
from telegram import Bot
from telegram.error import TelegramError
import sqlite3

bot = Bot(token=TELEGRAM_BOT_TOKEN)
YOUR_CHAT_ID = 123456789  # ← Your Telegram ID here

async def periodic_analysis():
    try:
        action, confidence, reasons = analyze_market()
        logging.info(f"Market analyzed. Action: {action} ({confidence}%)")

        try:
            save_signal(action, confidence)
        except sqlite3.Error as db_err:
            logging.error(f"SQLite error: {db_err}")

        if confidence >= SIGNIFICANCE_THRESHOLD_HIGH:
            try:
                text = f"[BTC/USDT]\n🚨 Action: {action} ({confidence:.1f}%)\nReasons:\n" + "\n".join(f"- {r}" for r in reasons)
                await bot.send_message(chat_id=YOUR_CHAT_ID, text=text)
                logging.info("🔔 High-confidence signal sent")
            except TelegramError as tg_err:
                logging.error(f"Telegram API error (high confidence): {tg_err}")

        elif confidence >= SIGNIFICANCE_THRESHOLD_MID:
            recent = get_recent_signals(SIGNIFICANCE_DURATION_MINUTES)
            if all(x[1] == action and x[2] >= SIGNIFICANCE_THRESHOLD_MID for x in recent):
                try:
                    text = f"[BTC/USDT]\n⚠️ Sustained signal: {action} ({confidence:.1f}%)"
                    await bot.send_message(chat_id=YOUR_CHAT_ID, text=text)
                    logging.info("🔔 Sustained mid-confidence signal sent")
                except TelegramError as tg_err:
                    logging.error(f"Telegram API error (mid confidence): {tg_err}")

    except Exception as e:
        logging.error(f"❌ Unexpected error during periodic analysis: {e}")

def main():
    setup_logger()
    logging.info("🔄 Starting CryptoSentinel bot...")
    init_db()
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: asyncio.run(periodic_analysis()), 'interval', minutes=ANALYSIS_INTERVAL_MINUTES)
    scheduler.start()
    start_bot()

if __name__ == "__main__":
    main()
