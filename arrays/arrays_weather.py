from parsers import Moscow, URL_MONTH, URL

moscow = Moscow()

html_today = moscow.get_html(URL)
today = moscow.get_today_content(html_today.text)
weather_today_list = [
    f"{today[0]['date']}: {today[0]['weather']}\n",
    f"Сегодня в {today[1]['date']}: {today[1]['weather']}\n",
    f"А завтра в {today[2]['date']} будет: {today[2]['weather']}\n",
]

html_month = moscow.get_html(URL_MONTH)
month = moscow.get_month(html_month.text)
weather_month_list = [
    f"{month[0]['date']}: {month[0]['weather']}, ночью {month[0]['night']}",
    f"{month[1]['date']}: {month[1]['weather']}, ночью {month[1]['night']}",
    f"{month[2]['date']}: {month[2]['weather']}, ночью {month[2]['night']}",
    f"{month[3]['date']}: {month[3]['weather']}, ночью {month[3]['night']}",
    f"{month[4]['date']}: {month[4]['weather']}, ночью {month[4]['night']}",
    f"{month[5]['date']}: {month[5]['weather']}, ночью {month[5]['night']}",
    f"{month[6]['date']}: {month[6]['weather']}, ночью {month[6]['night']}",
    f"{month[7]['date']}: {month[7]['weather']}, ночью {month[7]['night']}",
    f"{month[8]['date']}: {month[8]['weather']}, ночью {month[8]['night']}",
    f"{month[9]['date']}: {month[9]['weather']}, ночью {month[9]['night']}",
    f"{month[10]['date']}: {month[10]['weather']}, ночью {month[10]['night']}",
    f"{month[11]['date']}: {month[11]['weather']}, ночью {month[11]['night']}",
    f"{month[12]['date']}: {month[12]['weather']}, ночью {month[12]['night']}",
    f"{month[13]['date']}: {month[13]['weather']}, ночью {month[13]['night']}",
    f"{month[14]['date']}: {month[14]['weather']}, ночью {month[14]['night']}",
    f"{month[15]['date']}: {month[15]['weather']}, ночью {month[15]['night']}",
    f"{month[16]['date']}: {month[16]['weather']}, ночью {month[16]['night']}",
    f"{month[17]['date']}: {month[17]['weather']}, ночью {month[17]['night']}",
    f"{month[18]['date']}: {month[18]['weather']}, ночью {month[18]['night']}",
    f"{month[19]['date']}: {month[19]['weather']}, ночью {month[19]['night']}",
    f"{month[20]['date']}: {month[20]['weather']}, ночью {month[20]['night']}",
    f"{month[21]['date']}: {month[21]['weather']}, ночью {month[21]['night']}",
    f"{month[22]['date']}: {month[22]['weather']}, ночью {month[22]['night']}",
    f"{month[23]['date']}: {month[23]['weather']}, ночью {month[23]['night']}",
    f"{month[24]['date']}: {month[24]['weather']}, ночью {month[24]['night']}",
    f"{month[25]['date']}: {month[25]['weather']}, ночью {month[25]['night']}",
    f"{month[26]['date']}: {month[26]['weather']}, ночью {month[26]['night']}",
    f"{month[27]['date']}: {month[27]['weather']}, ночью {month[27]['night']}",
    f"{month[28]['date']}: {month[28]['weather']}, ночью {month[28]['night']}",
    f"{month[29]['date']}: {month[29]['weather']}, ночью {month[29]['night']}",
    f"{month[30]['date']}: {month[30]['weather']}, ночью {month[30]['night']}",
]
