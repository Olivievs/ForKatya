import logging
import asyncio
from telegram import Update
from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from ml.models import TextTranslationResult
from ml.ml_model.analyze import analyze

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Send me message")



async def get_emote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text
    loop = asyncio.get_event_loop()
    mes = await loop.run_in_executor(None, analyze, text)
    result = mes
    obj = TextTranslationResult(
        input_text=text,
        output_text=result
    )
    await loop.run_in_executor(None, obj.save)
    await context.bot.send_message(chat_id=chat_id, text=result)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        application = ApplicationBuilder().token(settings.TOKEN).build()
        start_handler = CommandHandler('start', start)
        application.add_handler(start_handler)
        emote = MessageHandler(filters.TEXT & (~filters.COMMAND), get_emote)
        application.add_handler(emote)

        application.run_polling()

