import logging

from aiogram.types import Message, CallbackQuery
from loader import dp
from aiogram.dispatcher.filters import Command
from keyboards.inline.choise_buttons import choice
from keyboards.inline.calback_datas import buy_callback
from keyboards.inline.choise_buttons import pear_keyboard, apples_keyboard, google_keyboard, cancel_button


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text="на продажу: ",
                         reply_markup=choice
                         )


@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    # посмотреть что внутри
    logging.info(f"call == {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали яблоко, спасибо {quantity}",
                              reply_markup=apples_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name="pear"))
async def buying_pear(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    # посмотреть что внутри
    # callback_data = call.data
    logging.info(f"call == {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали грушу, спасибо {quantity}",
                              reply_markup=pear_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name="google"))
async def buying_google(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call == {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали гугл, спасибо {quantity}",
                              reply_markup=google_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("Вы отменили покупку")
    # обращаюсь к сообщению к которому была прикреплена эта кнопка
    await call.message.edit_reply_markup(reply_markup=None)
