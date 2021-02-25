from loader import bot
from aiogram import executor


async def on_shutdown():
    await bot.close()


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_shutdown=on_shutdown)
