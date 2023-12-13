import asyncio
import json
import aiohttp


BASE_URL = "https://api.themoviedb.org/3"
API_KEY = "d2f58f193ec10f64760e31baa52fd192"


async def fetch_movies(session, url):
    async with session.get(url) as response:
        return await response.json()


async def get_movies(limit_results=None):
    page = 1
    all_movies = []
    async with aiohttp.ClientSession() as session:
        try:
            while True:
                url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&page{page}&include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
                data = await fetch_movies(session, url)
                movies_by_page = data.get("results", [])

                if not movies_by_page:
                    break

                all_movies += movies_by_page

                if (
                    len(all_movies) >= limit_results
                    if limit_results
                    else data.get("total_results")
                ):
                    break
                page += 1

        except Exception as err:
            print(f"An error occurred: {err}")
    return all_movies


async def main():
    movies = await get_movies(50)
    with open("movies.json", "w", encoding='UTF-8') as file:
        json.dump(movies, file, indent=4)
        print("movies saved to file")


if __name__ == "__main__":
    asyncio.run(main())
