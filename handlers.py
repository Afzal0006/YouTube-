from telegram import Update
from telegram.ext import ContextTypes
from downloader import download_youtube
from utils import file_size
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎶 Welcome to YouTube Downloader Bot!\n\n"
        "Use:\n"
        "/video <url> - Download video\n"
        "/audio <url> - Download audio"
    )

async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("❌ Please provide a YouTube link!")

    url = context.args[0]
    await update.message.reply_text("⏳ Downloading video...")
    file_path = download_youtube(url, audio=False)
    size = file_size(file_path)

    if size > 1900:  # 2GB Telegram limit approx
        await update.message.reply_text("❌ File too large for Telegram!")
    else:
        await update.message.reply_video(video=open(file_path, "rb"))
    
    os.remove(file_path)

async def audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("❌ Please provide a YouTube link!")

    url = context.args[0]
    await update.message.reply_text("⏳ Downloading audio...")
    file_path = download_youtube(url, audio=True)
    size = file_size(file_path)

    if size > 1900:
        await update.message.reply_text("❌ File too large for Telegram!")
    else:
        await update.message.reply_audio(audio=open(file_path, "rb"))
    
    os.remove(file_path)
