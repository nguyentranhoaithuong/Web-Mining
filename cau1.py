import requests
from bs4 import BeautifulSoup
import os
url="http://vanhoanghethuat.vn/di-san.chtm"
link_todo=[url]

for i in range(2,16):
    a="http://vanhoanghethuat.vn/di-san.chtm?CatID=178&page="+str(i)
    link_todo+=[a]
filename=os.path.join("E:\Code\KPW", "Cau1.txt")    
with open(filename, 'w', encoding='utf-8') as f:
    for link in link_todo:
        f.write(link + "\n")