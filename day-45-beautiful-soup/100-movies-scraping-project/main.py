import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# getting the url text
response = requests.get(URL)
empire_text = response.text
soup = BeautifulSoup(empire_text, "html.parser")

# get all the titles in a list from 1 to 100
titles = soup.find_all(name="h3", class_="title")
titles_list = [title.getText() for title in titles[::-1]]

# save the titles to a text file
with open("titles.txt", "w") as textfile:
    for item in titles_list:
        textfile.write(item + "\n")