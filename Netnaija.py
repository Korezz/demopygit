from bs4 import BeautifulSoup
import requests

page=requests.get('https://www.thenetnaija.net/videos/movies')

soup = BeautifulSoup(page.text, "lxml")

for data in soup.find_all("article", class_="file-one shadow"):

    title = data.img['title']
    print("MOVIE TITLE")
    print(title)
    print()

    vid_link = data.h2.a['href']
    print('VIDEO LINK')
    print(vid_link)
    print()

    rel_data = data.span['title']
    rel_data = rel_data.split('T')
    print("UPLOADED DATE")
    print(rel_data)
    print()
    print()
    print()