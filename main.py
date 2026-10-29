import asyncio
from aiogram import Bot, Dispatcher
from aiogram.exceptions import (
    TelegramNetworkError,
    TelegramUnauthorizedError,
)
from config.settings import BOT_TOKEN
from handlers.users.start import rt as star
from handlers.users.date import rt as date
from handlers.users.test import rt as test
from handlers.users.sana import rt as sana
from handlers.users.shting import rt as shting
from handlers.users.video import rt as video
from handlers.users.txt import rt as txt
from handlers.users.uzbek import rt as uzbek
from handlers.users.malumot import rt as malumotlar
from handlers.users.photo import rt as photo
from handlers.users.it import rt as it
from handlers.users.mishq import rt as mishq
from handlers.users.rasm import rt as rasm
from handlers.users.help import rt as help
dp = Dispatcher()
async def main():
    bot = Bot(BOT_TOKEN)
    dp.include_router(star)
    dp.include_router(help)
    dp.include_router(date)
    dp.include_router(sana)
    dp.include_router(shting)
    dp.include_router(malumotlar)
    dp.include_router(photo)
    dp.include_router(video)
    dp.include_router(it)
    dp.include_router(uzbek)
    dp.include_router(txt)
    dp.include_router(mishq)
    dp.include_router(rasm)
    dp.include_router(test)
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("bot ishga tushdi")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot to'xtatildi")
    except TelegramNetworkError:
        print("internetga yo'q")
    except TelegramUnauthorizedError:
        print("token xato!")
