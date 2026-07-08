import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚛 Bine ai venit la RETUR TIR ROMÂNIA!\n\nBotul este online și funcționează!"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Botul a pornit...")
    app.run_polling()

if __name__ == "__main__":
    main()
