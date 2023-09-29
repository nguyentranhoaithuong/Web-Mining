import requests
from bs4 import BeautifulSoup
import os
url = "http://vanhoanghethuat.vn/di-san.chtm"
link_todo = [url]

for i in range(2, 16):
    a = "http://vanhoanghethuat.vn/di-san.chtm?CatID=178&page=" + str(i)
    link_todo.append(a)
filename=os.path.join("E:\Code\KPW","Cau2.txt")
with open(filename, "w", encoding="utf-8") as file:
    for i in range(15):
        l = link_todo[i]
        html = requests.get(l).text
        soup = BeautifulSoup(html, "html5lib")
        tenlink = soup.find_all("div", class_="post-entry")
        for entry in tenlink:
            tl = entry.find("a")
            href = tl.get("href")
            file.write("http://vanhoanghethuat.vn" + href + "\n")
            print("http://vanhoanghethuat.vn" + href)





