import json

import requests

URL = "https://jsonplaceholder.typicode.com/posts/1/comments"

response = requests.get(URL, timeout=(5, 5))
data = response.json()

sorted_data = sorted(data, key=lambda x: x["name"])

with open("comments.json", "w", encoding="UTF-8") as file:
    file.write(json.dumps(sorted_data, indent=4))
