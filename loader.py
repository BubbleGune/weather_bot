import logging
from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from config import BOT_TOKEN

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] \
                    #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)
