from selenium import webdriver
from bs4 import BeautifulSoup

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('./chromedriver')


driver.implicitly_wait(3)

driver.get('https://www.gdax.com/trade/BTC-USD')


