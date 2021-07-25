import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

# load_url = "https://www.ymori.com/books/python2nen/test1.html"
# load_url = "http://or0e9abi5m.php.xdomain.jp/myblog/index.php"
# load_url = "https://illionillion.github.io/rinkustudentsteam/"
load_url = "http://or0e9abi5m.php.xdomain.jp/myblog/search_contents.php?keyword=%E3%82%A2%E3%83%8B%E3%83%A1"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
# print(soup)

ele_title=soup.find('title')
print(ele_title.text)
# print(soup.find_all('li'))

# intro_body=soup.find(id='intro_body')
# print(intro_body)

ulele=soup.find('ul',class_='section-list')
# print(ulele.contents)

for child in ulele.children:
  print(child)
  # liele=child.find('li')
  # aele=liele.find('a')
  # print(aele)


# print(ulele)