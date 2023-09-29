
import requests
from bs4 import BeautifulSoup
import os

# Tạo thư mục để lưu trữ file văn bản
if not os.path.exists('output'):
    os.mkdir('output')

url = "http://vanhoanghethuat.vn/di-san.chtm"
link_todo = [url]
L = ['di-san.chtm']

for i in range(2, 16):
    a = "http://vanhoanghethuat.vn/di-san.chtm?CatID=178&page=" + str(i)
    b = 'di-san.chtm_CatID=178&page=' + str(i)
    link_todo+=[a]
    L+=[b]

for i in range(15):
    l = link_todo[i]
    html = requests.get(l).text
    soup = BeautifulSoup(html, "html5lib")
    ten = soup.find_all('h2', class_="post-box-title")
    tomtat = soup.find_all('p', class_="post-excerpt")

    for j in L:
        # Loại bỏ các ký tự không hợp lệ trong tên file
        filename = f'output/http-vanhoanghethuat.vn{j}.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            for k in range(len(ten)):
                file.write("Tiêu đề: " + ten[k].text + "\n")
                file.write("Tóm tắt: " + tomtat[k].text + "\n")
