import json
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "04f07c499bfaf8b2b85bf866099fa06a"


def get_weather(city="Lviv"):
    url = f"{BASE_URL}?q={city}&units=metric&appid={API_KEY}"
    try:
        response = requests.get(url, timeout=(5, 5))

        data = json.loads(response.text)

        if data["cod"] in [200, "200"]:
            print(
                "-------------------------",
                f'Weather in {data["name"]}, {data["sys"]["country"]}:',
                f'Temp.: {round(data["main"]["temp"])}°C',
                f'Feels_like: {round(data["main"]["feels_like"])}°C',
                f'Weather description: {data["weather"][0]["description"]}',
                "Wind:",
                f'\t Speed: {data["wind"]["speed"]} m/s',
                f'\t Gust: {data["wind"].get("gust", "-")} m/s',
                f'Pressure: {round(data["main"]["pressure"] * 0.750062)} mm',
                f'Humidity: {data["main"]["humidity"]} %',
                "-------------------------",
                sep="\n",
                end="\n\n",
            )

        elif data["cod"] in [404, "404"]:
            print(f'City with name "{city}" not found!')
        else:
            print(
                f'Something went wrong! Response with code {data["cod"]}: {data.get("message", "")}'
            )

    except ConnectionError as err:
        print(f"Connection error! {err}")


if __name__ == "__main__":
    while True:
        city_name = None
        while not city_name:
            city_name = input("Enter city name: ")

        get_weather(city_name)
