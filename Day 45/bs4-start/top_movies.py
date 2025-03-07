from bs4 import BeautifulSoup
import requests

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_web_page=response.text

soup=BeautifulSoup(movie_web_page,"html.parser")
movies=soup.find_all(name='h3', class_='title')
movie_text=[]
for movie in movies:
    movie_text.append(movie.getText())

with open('movies.txt',mode='w',encoding="utf-8") as file:

    for n in range(len(movie_text)-1,-1,-1):
        file.write(f"{movie_text[n]}\n")
