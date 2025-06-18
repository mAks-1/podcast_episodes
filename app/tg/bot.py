import os
import logging
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "http://app:8000")


bot = Bot(
    token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привіт! Надішли команду в форматі:\n<code>/alt &lt;id&gt; &lt;prompt&gt;</code>\nНаприклад:\n<code>/alt 1 Перепиши опис для Gen Z</code>"
    )
