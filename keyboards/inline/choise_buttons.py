from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# from keyboards.inline.calback_datas import buy_callback

from config import URL_APPLE, URL_PEAR, URL_GOOGLE

"""
choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(
                item_name="pear", quantity=1
            )),
            InlineKeyboardButton(text="Купить не грушу", callback_data="buy:apple:5"),
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ]
)
"""

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Купить грушу", callback_data="buy:pear:5")
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Купить яблоки", callback_data="buy:apple:1")
choice.insert(buy_apples)

buy_google = InlineKeyboardButton(text="Купить гугл", callback_data="buy:google:1")
choice.insert(buy_google)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купи тут", url=URL_PEAR)
        ]
    ]
)
apples_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купи тут", url=URL_APPLE)
        ]
    ]
)
google_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купи тут", url=URL_GOOGLE)
        ]
    ]
)
