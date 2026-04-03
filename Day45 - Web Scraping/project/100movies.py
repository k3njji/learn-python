import requests
from bs4 import BeautifulSoup
# import json

def get_top_100_movies():
    url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
    response = requests.get(url)

    print(response.status_code)
    print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())

    movie_titles = soup.find_all("h3", class_="title")
    movie_title = [movie.get_text() for movie in movie_titles[::-1]]

    with open('Day45 - Web Scraping/project/top_100_movies.txt', mode='w', encoding='utf-8') as file:
        for title in movie_title:
            file.write(title + "\n")
        file.close()


get_top_100_movies()
    