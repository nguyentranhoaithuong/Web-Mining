
import requests
from bs4 import BeautifulSoup
import os
if not os.path.exists('html'):
    os.mkdir('html')
url = "http://vanhoanghethuat.vn/di-san.chtm"
link_todo = [url]
L = ['di-san.chtm']
for i in range(2, 16):
    a = "http://vanhoanghethuat.vn/di-san.chtm?CatID=178&page=" + str(i)
    b = 'di-san.chtm_CatID=178&page=' + str(i)
    link_todo+=[a]
    L+=[b]
for i in range(0,15):
    l = link_todo[i]
    html = requests.get(l).text
    filename = f'html/http-vanhoanghethuat.vn{L[i]}.html'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html)


