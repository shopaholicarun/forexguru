# -*- coding: utf-8 -*-
"""
Web automation trials
Using Selenium and BeautifulSoup, 
Find th


@author: Arun Kumar Elakoran
"""
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://www.xe.com')

val = driver.find_element_by_xpath('//*[@id="amount"]')
val.send_keys('1000')
fromcurr=driver.find_element_by_xpath('//*[@id="converterForm"]/form/div[2]/div/div/div[1]/div[1]')
tocurr=driver.find_element_by_xpath('//*[@id="converterForm"]/form/div[2]/div/div/div[1]')


submit=driver.find_element_by_xpath('//*[@id="converterForm"]/form/button[2]')
submit.click()





#val=driver.find_element_by_xpath('//*[@id="converterResult"]/div/div/div[2]/span[1]').get_Attribute("converterresult-toAmount")

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

spans = soup.findAll('span', attrs={'class': 'converterresult-toAmount'})
spans = soup.find_all(class_=re.compile("converterresult-toAmount"))

usd2euro=spans[0].text

print(f"1 USD is {usd2euro} EUROS")
