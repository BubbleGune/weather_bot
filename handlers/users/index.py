from aiogram.types import Message
from loader import dp
from parsers import Moscow, URL
from arrays import weather_month_list


@dp.message_handler(commands=["start", "help"])
async def send_a_greeting(message: Message):
    await message.answer(text="Привет, я бот с погодой по городу Москве.\n\n"
                              "Вот что я могу:\n"
                              "Показать погоду на сегодня команда: /today\n"
                              "Показать погоду в Москве на месяц: /month")


@dp.message_handler(commands=["today"])
async def send_today(message: Message):
    today = Moscow()
    html = today.get_html(URL)
    await message.answer(text=f"{today.get_today_content(html.text)[0]['date']}: "
                              f"{today.get_today_content(html.text)[0]['weather']}\n"
                              f"Сегодня в {today.get_today_content(html.text)[1]['date']}: "
                              f"{today.get_today_content(html.text)[1]['weather']}\n"
                              f"А уже завтра в {today.get_today_content(html.text)[1]['date']}: "
                              f"Будет {today.get_today_content(html.text)[1]['weather']}")


@dp.message_handler(commands=["month"])
async def send_weather_month(message: Message):
    await message.answer(text=f"{weather_month_list[0]}\n"
                              f"{weather_month_list[1]}\n"
                              f"{weather_month_list[2]}\n"
                              f"{weather_month_list[3]}\n"
                              f"{weather_month_list[4]}\n"
                              f"{weather_month_list[5]}\n"
                              f"{weather_month_list[6]}\n"
                              f"{weather_month_list[7]}\n"
                              f"{weather_month_list[8]}\n"
                              f"{weather_month_list[9]}\n"
                              f"{weather_month_list[10]}\n"
                              f"{weather_month_list[11]}\n"
                              f"{weather_month_list[12]}\n"
                              f"{weather_month_list[13]}\n"
                              f"{weather_month_list[14]}\n"
                              f"{weather_month_list[15]}\n"
                              f"{weather_month_list[16]}\n"
                              f"{weather_month_list[17]}\n"
                              f"{weather_month_list[18]}\n"
                              f"{weather_month_list[19]}\n"
                              f"{weather_month_list[20]}\n"
                              f"{weather_month_list[21]}\n"
                              f"{weather_month_list[22]}\n"
                              f"{weather_month_list[23]}\n"
                              f"{weather_month_list[24]}\n"
                              f"{weather_month_list[25]}\n"
                              f"{weather_month_list[26]}\n"
                              f"{weather_month_list[27]}\n"
                              f"{weather_month_list[28]}\n"
                              f"{weather_month_list[29]}\n"
                              f"{weather_month_list[30]}\n"
                         )
