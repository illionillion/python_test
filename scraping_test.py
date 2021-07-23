import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

# load_url = "https://www.ymori.com/books/python2nen/test1.html"
# load_url = "http://or0e9abi5m.php.xdomain.jp/myblog/index.php"
load_url = "https://illionillion.github.io/rinkustudentsteam/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
# print(soup)

ele_title=soup.find('title')
print(ele_title.text)
# print(soup.find_all('li'))

intro_body=soup.find(id='intro_body')
print(intro_body)