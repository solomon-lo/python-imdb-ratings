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

    