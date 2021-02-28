import requests
from bs4 import BeautifulSoup
import csv

HOST = "https://www.gismeteo.ru/"
URL = "https://www.gismeteo.ru/weather-moscow-4368/"
HEADERS = {
    "accept-encoding": "gzip, deflate, br",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}


def get_html(url, params=""):
    response = requests.get(url, headers=HEADERS, params=params)
    return response

# html = get_html(URL)


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="tab_wrap")
    cards = []

    for item in items:
        cards.append(
            {
                "date": item.find("div", class_="date").get_text(strip=True),
                "weather": item.find("span", class_="unit").get_text(strip=True),
            }
        )
    return cards


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        pass
    else:
        print("Error")

# html = get_html(URL)
# print(get_content(html.text)[2])
