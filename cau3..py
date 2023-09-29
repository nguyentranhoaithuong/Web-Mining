import requests
from bs4 import BeautifulSoup
import os
url="http://vanhoanghethuat.vn/di-san.chtm"
link_todo=[url]
for i in range(2,16):
    a="http://vanhoanghethuat.vn/di-san.chtm?CatID=178&page="+str(i)
    link_todo+=[a]
str= " "
for i in range(0,15):
    l=link_todo[i]
    html=requests.get(l).text
    soup=BeautifulSoup(html,"html5lib")
    ten=soup.find_all('h2',class_="post-box-title")
    tomtat=soup.find_all('p',class_="post-excerpt")
    for j in range(1,len(ten)-1):
        str+= "Tiêu đề:"+ten[j].text +"\n"
        str+= "Tóm tắt: "+tomtat[j].text +"\n"
    print(str)
    filename=os.path.join("E:\Code\KPW\chapter2","3.txt")
    with open(filename,'w',encoding='utf-8') as f:
        f.write(str)
