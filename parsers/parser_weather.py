import requests
from bs4 import BeautifulSoup

HOST = "https://www.gismeteo.ru/"
URL = "https://www.gismeteo.ru/weather-moscow-4368/now/"
URL_MONTH = "https://www.gismeteo.ru/weather-moscow-4368/month/"


class Moscow:
    def __init__(self):
        self.HEADERS = {
            "accept-encoding": "gzip, deflate, br",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
        }

    def get_html(self, url, params=""):
        response = requests.get(url, headers=self.HEADERS, params=params)
        return response

    @staticmethod
    def get_today_content(html) -> list:
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all("div", class_="tab_wrap")
        cards = []

        for item in items:
            cards.append(
                {
                    "date": item.find("div", class_="tab-content").find(class_="date").get_text(strip=True),
                    "weather": item.find("span", class_="unit").get_text(strip=True)
                }
            )
        return cards

    @staticmethod
    def get_month(html) -> list:
        soup = BeautifulSoup(html, "html.parser")
        first_day_month = soup.find_all("div", class_="tooltip cell past")
        first_two_week = soup.find_all("div", class_="tooltip cell _hover")
        last_two_week = soup.find_all("div", class_="tooltip cell")
        array = []

        for item in first_day_month:
            array.append(
                {
                    "date": item.find("div", class_="date").get_text(strip=True),
                    "weather": item.find("div", class_="temp_max js_meas_container").find(
                        class_="value unit unit_temperature_c").get_text(strip=True),
                    "night": item.find("div", class_="temp_min js_meas_container").find(
                        class_="value unit unit_temperature_c").get_text(strip=True)
                }
            )

        for item in first_two_week:
            array.append(
                {
                    "date": item.find("span").get_text(strip=True),
                    "weather": item.find("span", class_="value unit unit_temperature_c").get_text(strip=True),
                    "night": item.find("span", class_="js_value val_to_convert").find("span").get_text(strip=True)
                }
            )

        for item in last_two_week:
            array.append(
                {
                    "date": item.find("div", class_="date").get_text(strip=True),
                    "weather": item.find("span", class_="value unit unit_temperature_c").get_text(strip=True),
                    "night": item.find("div", class_="temp_min js_meas_container").find(
                        class_="unit_temperature_c").get_text(strip=True)
                }
            )
        return array
