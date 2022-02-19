from datetime import datetime
import omdb
import requests
import os


def _resume_text(text: str, length: int) -> str:
    return text[:text[:length - 1].rfind(".") + 1] if len(text) >= length else text


def _text_to_datetime(text: str, datetime_format: str) -> [datetime, None]:
    try:
        return datetime.strptime(text, datetime_format)
    except ValueError:
        return None


def _text_to_float(text: str) -> [float, None]:
    try:
        return float(text)
    except ValueError:
        return None


def _text_to_integer(text: str) -> [int, None]:
    try:
        return int(text)
    except ValueError:
        return None


def main():
    str_titles = os.environ.get("TITLES", 'Game of Thrones, Peaky Blinders, Skins')
    api_load_balancer_name = os.environ.get("API_LOAD_BALANCER_NAME", "localhost:8000")
    api_key = os.environ.get("API_KEY", 'fc9ab012')
    client = omdb.Api(apikey=api_key)
    api_titles = [e["title"] for e in requests.get(f"http://{api_load_balancer_name}/titles/").json()]
    titles = [e.strip() for e in str_titles.split(",")]
    titles_missing = sorted(set(titles) - set(api_titles))
    titles_exceeding = sorted(set(api_titles) - set(titles))

    for title_missing in titles_missing:
        client_title = client.search(title=title_missing).json()
        client_title_exists = client_title["Response"] == "True"

        print(f"Adding {title_missing}!")
        if client_title_exists:
            client_title_imdb_id = client_title["imdbID"]
            client_title_number_of_seasons = int(client_title["totalSeasons"])
            client_title_genres = [e.strip() for e in client_title["Genre"].split(",")]
            client_title_languages = [e.strip() for e in client_title["Language"].split(",")]
            client_title_plot = _resume_text(text=client_title["Plot"], length=256)
            client_title_imdb_rating = _text_to_float(client_title["imdbRating"])
            client_title_released_datetime = _text_to_datetime(client_title["Released"], "%d %b %Y")
            title_data = {
                "imdb_id": client_title_imdb_id,
                "title": client_title["Title"],
                "plot": client_title_plot,
                "poster": client_title["Poster"],
                "imdb_rating": client_title_imdb_rating,
            }
            response = requests.post(f"http://{api_load_balancer_name}/titles/", data=title_data)

            if not response.ok:
                print("ERROR", client_title_imdb_id, response.json())

            title_release_data = {
                "release_owner_title": client_title_imdb_id,
            }

            if isinstance(client_title_released_datetime, datetime):
                title_release_data["day"] = client_title_released_datetime.day
                title_release_data["month"] = client_title_released_datetime.month
                title_release_data["year"] = client_title_released_datetime.year

            response = requests.post(f"http://{api_load_balancer_name}/title_releases/", data=title_release_data)

            if not response.ok:
                print("ERROR", client_title_imdb_id, response.json())
            for client_title_genre in client_title_genres:
                genre_data = {
                    "name": client_title_genre,
                    "genre_owner_title": client_title_imdb_id,
                }
                response = requests.post(f"http://{api_load_balancer_name}/genres/", data=genre_data)

                if not response.ok:
                    print("ERROR", client_title_genre, response.json())
            for client_title_language in client_title_languages:
                language_data = {
                    "name": client_title_language,
                    "language_owner_title": client_title_imdb_id,
                }
                response = requests.post(f"http://{api_load_balancer_name}/languages/", data=language_data)

                if not response.ok:
                    print("ERROR", client_title_language, response.json())
            for season_number in range(1, client_title_number_of_seasons + 1):
                client_season = client.search(title=title_missing, season=season_number).json()
                client_season_episodes = client_season["Episodes"]
                season_data = {
                    "season_number": season_number,
                    "season_owner_title": client_title_imdb_id,
                }
                response = requests.post(f"http://{api_load_balancer_name}/seasons/", data=season_data)

                if not response.ok:
                    print("ERROR", season_number, response.json())
                else:
                    api_season = response.json()

                    for client_season_episode in client_season_episodes:
                        client_season_episode_imdb_id = client_season_episode["imdbID"]
                        client_season_episode = client.search(imdb_id=client_season_episode_imdb_id).json()
                        client_season_episode_plot = _resume_text(text=client_season_episode["Plot"], length=256)
                        client_season_episode_rating = _text_to_float(client_season_episode["imdbRating"])
                        client_season_episode_released_datetime = _text_to_datetime(client_season_episode["Released"],
                                                                                    '%d %b %Y')
                        episode_data = {
                            "imdb_id": client_season_episode_imdb_id,
                            "episode_owner_title": client_title_imdb_id,
                            "title": client_season_episode["Title"],
                            "episode_number": client_season_episode["Episode"],
                            "runtime": _text_to_integer(client_season_episode["Runtime"].split()[0]),
                            "plot": client_season_episode_plot,
                            "poster": client_season_episode["Poster"],
                            "imdb_rating": client_season_episode_rating,
                            "episode_owner_season": api_season["id"],
                        }
                        response = requests.post(f"http://{api_load_balancer_name}/episodes/", data=episode_data)

                        if not response.ok:
                            print("ERROR", client_season_episode_imdb_id, response.json())

                        episode_release_data = {
                            "release_owner_episode": client_season_episode_imdb_id,
                        }

                        if isinstance(client_season_episode_released_datetime, datetime):
                            episode_release_data["day"] = client_season_episode_released_datetime.day
                            episode_release_data["month"] = client_season_episode_released_datetime.month
                            episode_release_data["year"] = client_season_episode_released_datetime.year

                        requests.post(f"http://{api_load_balancer_name}/episode_releases/", data=episode_release_data)
        else:
            print(f"{title_missing} does not exist on client! Aborting add!")

    for title_exceeding in titles_exceeding:
        response = requests.get(f"http://{api_load_balancer_name}/titles/title/{title_exceeding}")

        print(f"Removing {title_exceeding}!")
        if not response.ok:
            print("ERROR", title_exceeding, response.json())
        else:
            api_title = response.json()
            api_title_imdb_id = api_title["imdb_id"]

            requests.delete(f"http://{api_load_balancer_name}/titles/{api_title_imdb_id}")


if __name__ == '__main__':
    main()
