from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome('C:\scraping_chromedriver\chromedriver')
# driver = webdriver.Chrome('C:\scraping_chromedriver\chromedriver')

driver.get('https://illionillion.github.io/novelgameproject2021/index.html')

#リンクテキスト名が"画像"の要素を取得
# title_btn_element = driver.find_elements_by_tag_name("input")
title_btn_element = driver.find_element_by_xpath('//div[@id="title_btn"]/div[1]/input')
#画像のリンクをクリック
title_btn_element.click()
print(title_btn_element)

for i in range(0,13):
  controller_btn_element=driver.find_element_by_xpath('//div[@id="controller_frame"]/div[2]/input')
  controller_btn_element.click()
Alert(driver).accept()

# driver.close()
# driver.quit()