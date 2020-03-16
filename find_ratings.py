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
    x = line.split(", ")
    title = line.lower()
    release = x[1]
    query = "+".join(title.split()) 
    URL = "https://www.imdb.com/search/title/?title=" + query
    print(URL)
    # print(release)
    try: 
        response = s.get(URL)

        #getting contect from IMDB Website
        content = response.content
        print(content)