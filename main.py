from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-century/").text

soup = BeautifulSoup(response, "html.parser")

titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

movie_titles = [title.getText() for title in titles]
movie_titles.reverse()
# var = movie_titles[::-1]

movie_titles[1] = "2) The Lord Of The Rings: The Fellowship Of The Ring"

with open("100 Movies To Watch.txt", "w") as file:
    for title in movie_titles:
        file.write(f"{title}\n")
