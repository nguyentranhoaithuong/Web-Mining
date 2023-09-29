from bs4 import BeautifulSoup
import requests
import re
import emot
import nltk
import os
from textblob import TextBlob
from nltk.corpus import stopwords
url = "https://edition.cnn.com/business"
link_todo = []
count=0
str=' '
html = requests.get(url).text
soup = BeautifulSoup(html, "html5lib")
article_links = soup.find_all("div",class_="container__field-links container_grid-4__field-links")
link=article_links[2].find_all('a',class_="container__link container_grid-4__link")
# print(len(article_links))
for i in range(len(link)):
    a=link[i].get("href")
    l="https://edition.cnn.com"+a
    if l not in link_todo:
        link_todo=link_todo+[l]
for i in range(len(link_todo)):
    count=count+1
    article=link_todo[i]
    h=requests.get(article).text
    s=BeautifulSoup(h,'html5lib')
    nd=s.find_all('p',class_="paragraph inline-placeholder")
    # print(nd)
    for i in range(len(nd)):
        str+=nd[i].text
        # sửa chính tả
    text1=TextBlob(str).correct()
    # chữ thường
    text1=text1.lower()
    # xóa stopword
    stop=stopwords.words('english')
    text1 = " ".join(text for text in text1.split() if text not in stop)
    # xóa chữ số
    text2=re.sub(r'\d+',' ',text1)
    # emoji
    from emot.emo_unicode import UNICODE_EMOJI # For emojis
    from emot.emo_unicode import EMOTICONS_EMO # For EMOTICONS
    def converting_emojis(text2):
        for x in EMOTICONS_EMO:
            text2 = text2.replace(x, "_".join(EMOTICONS_EMO[x].replace(",","").replace(":","").split()))
        for x in UNICODE_EMOJI:
            text2 = text2.replace(x, "_".join(UNICODE_EMOJI[x].replace(",","").replace(":","").split()))
        return text2
    # tách câu
    text2 = nltk.sent_tokenize(text2)
    # xóa dấu câu
    text3=''
    for i in range(len(text2)):
        text3+=re.sub(r'[^\w\s]','',text2[i])
    # tách từ
    text=nltk.word_tokenize(text3)
    filename = f'output/page{count}.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(len(text)):
            file.write(text[i]+'\n')
    print(text)

    