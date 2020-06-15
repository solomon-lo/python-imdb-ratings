from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


s = requests.session()

films = []
names = []
ratings = []
genres = []

path = input("Input the file directory where you store your movies: ")

filmswe = os.listdir(path)

for film in filmswe:
    films.append(os.path.splitext(film)[0])
    print(os.path.splitext(film)[0])

for line in films:
    # x = line.split(", ")
    title = line.lower()
    # release = x[1]
    query = "+".join(title.split())
    URL = "https://www.imdb.com/search/title/?title=" + query
    print(URL)
    # print(release)
    try:
        response = s.get(URL)
        content = response.content


        soup = BeautifulSoup(response.content, features="html.parser")

        containers = soup.find_all("div", class_="lister-item-content")
        for result in containers:
            name1 = result.h3.a.text
            name = result.h3.a.text.lower()

            if title in name:
                rating = result.find(
                    "div", class_="inline-block ratings-imdb-rating")["data-value"]
                genre = result.p.find("span", class_="genre")
                genre = genre.contents[0]
    except Exception:
        print("Inputted title wasn't able to be found")
