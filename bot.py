from telegram.ext import Application, CommandHandler
from config import BOT_TOKEN
from handlers import start, video, audio

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("video", video))
    app.add_handler(CommandHandler("audio", audio))

    app.run_polling()

if __name__ == "__main__":
    main()
