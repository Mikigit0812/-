from bs4 import BeautifulSoup
import lxml
import requests
import urllib.request
print('ほしい人物名を入れてください')
name = input('>>')

#ソースコードを取る
headers = {"User-Agent": "hoge"}

URL = "https://search.yahoo.co.jp/image/search?p="+ name +"&fr=top_ga1_sa&ei=UTF-8#mode=search"
#mode=searchじゃないとうごかない？
resp = requests.get(URL, timeout=1, headers=headers)

#for i in range (num_pages):

soup = BeautifulSoup(resp.text,"lxml") #ソースコードをテキストで抽出
# print(soup.find_all("img")[0]["src"]) 

imgs = soup.find_all(alt="「"+ name + "」の画像検索結果")

for i in range (len(imgs)):
    filepath = name+"{}.png".format(i)
    urllib.request.urlretrieve(imgs[i]["src"],filepath)