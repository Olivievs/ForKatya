import logging
import asyncio
from telegram import Update
from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from ml.models import FatClassification
from ml.ml_model.analyze import analyze_obesity

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Отправьте данные одной строкой")



async def get_emote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text
    txt = str(text)
    loop = asyncio.get_event_loop()
    listing = txt.split(',')
    await context.bot.send_message(chat_id=chat_id, text=txt)
    await context.bot.send_message(chat_id=chat_id, text = listing)
    python_result = await loop.run_in_executor(None, FatClassification.to_model_style, listing)
    obj = FatClassification(
           python_result
       )
    mes = await loop.run_in_executor(None, analyze_obesity, python_result)
    result = mes
    await loop.run_in_executor(None, obj.analyze, result)
    await loop.run_in_executor(None, obj.save)
    await context.bot.send_message(chat_id=chat_id, text=obj.nobeyesdad)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        application = ApplicationBuilder().token(settings.TOKEN).build()
        start_handler = CommandHandler('start', start)
        application.add_handler(start_handler)
        emote = MessageHandler(filters.TEXT & (~filters.COMMAND), get_emote)
        application.add_handler(emote)

        application.run_polling()

