"""
Created on Mon Apr 27 18:05:02 2020

@author: Arun Kumar Elakoran

Learning Web Scraping 

This code will search the EURO2USD conversion rate in google and return what google gives


"""
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.google.com')

search = browser.find_element_by_name('q')
search.send_keys("1 EURO to USD")
search.send_keys(Keys.RETURN) # hit return after you enter search text

html=browser.page_source
soup=BeautifulSoup(html,'html.parser')

message=soup.findAll('div', attrs={'class': 'b1hJbf'})[0].text
print(message)



