import requests

URL = "https://translate.google.com/robots.txt"

response = requests.get(URL, timeout=(5, 5))

with open("robots.txt", "w", encoding="UTF-8") as file:
    file.write(response.text)
