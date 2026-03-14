from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from .gpt_service import generate_response


async def handle_message(update: Update, context):

    user_message = update.message.text

    response = generate_response(user_message)

    await update.message.reply_text(response)


def start_bot(token):

    app = ApplicationBuilder().token(token).build()

    app.add_handler(
        MessageHandler(filters.TEXT, handle_message)
    )

    app.run_polling()
