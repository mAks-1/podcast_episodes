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


@dp.message(Command("alt"))
async def generate_alternative(message: Message):
    try:
        parts = message.text.split(" ", 2)
        if len(parts) < 3:
            await message.answer("Формат команди: /alt <id> <prompt>")
            return

        episode_id = parts[1]
        prompt = parts[2]
        target = "title" if "title" in prompt.lower() else "description"

        payload = {"target": target, "prompt": prompt}

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{API_BASE_URL}/episodes/{episode_id}/generate_alternative",
                json=payload,
            ) as resp:
                if resp.status != 200:
                    text = await resp.text()
                    raise Exception(f"Error {resp.status}: {text}")
                data = await resp.json()

        await message.answer(
            f"<b>Епізод:</b> {data['original_episode']['title']}\n"
            f"<b>Запит:</b> {data['prompt']}\n\n"
            f"<b>Альтернатива:</b> {data['generated_alternative']}"
        )

    except Exception as e:
        logging.exception(e)
        await message.answer("Виникла помилка під час генерації. Спробуй ще раз.")


async def start_bot():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(start_bot())
