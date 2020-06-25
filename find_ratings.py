from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

#start a session
s = requests.session()

#arrays to hold data we will output to csv file
films = []
names = []
ratings = []
genres = []

#get input path where we will automatically get names to search for
path = input("Input the file directory where you store your movies: ")

filmswe = os.listdir(path)

#get each film's name by parsing file names
for film in filmswe:
    films.append(os.path.splitext(film)[0])
    print(os.path.splitext(film)[0])

#start data scraping
for line in films:
    title = line.lower()
    query = "+".join(title.split())
    #generate the correct url
    URL = "https://www.imdb.com/search/title/?title=" + query
    print(URL)
    try:
        response = s.get(URL)
        content = response.content

        #start html parser for BeautifulSoup
        soup = BeautifulSoup(response.content, features="html.parser")

        containers = soup.find_all("div", class_="lister-item-content")
        for result in containers:
            name1 = result.h3.a.text
            name = result.h3.a.text.lower()

            #get the titles needed
            if title in name:
                rating = result.find(
                    "div", class_="inline-block ratings-imdb-rating")["data-value"]
                genre = result.p.find("span", class_="genre")
                genre = genre.contents[0]
    except Exception:
        print("Inputted title wasn't able to be found")

df = pd.DataFrame({'Film Name':names,'Rating':ratings,'Genre':genres}) 

df.to_csv('film_ratings.csv', index=False, encoding='utf-8')
