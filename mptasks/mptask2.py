from concurrent.futures import ProcessPoolExecutor
import json
import requests


def get_comments(user_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{user_id}/comments"
    res = requests.get(url, timeout=(5, 5))
    return res.json()


if __name__ == "__main__":
    COMMENTS = {}

    with ProcessPoolExecutor() as executor:
        for index, data in zip(range(1, 6), executor.map(get_comments, range(1, 6))):
            COMMENTS[index] = data
            with open("comments.json", "w", encoding="UTF-8") as w_file:
                w_file.write(json.dumps(COMMENTS, indent=4))
