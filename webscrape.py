# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:13:44 2020

@author: Eric
"""
import re
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# setup options to make chrome headless
opts = Options()
opts.headless = True

# loads the chromedriver exe which opens a chrome window
driver = webdriver.Chrome(r'C:/chromedriver/chromedriver.exe', options=opts)

# comment out three lines above if chrome needs to be run with a head
#driver = webdriver.Chrome(r'C:/chomedriver/chromedriver.exe')

# loads the URL
driver.get('https://www.pathofexile.com/trade/search/Delirium')

# finds and clicks the search button
botton = driver.find_element_by_name('searchID')
botton.submit()

# convert the page to beautiful soup format
soup = bs(driver.page_source, 'html.parser')

# selects all table data
table = soup.findAll('div', {"class": "cbResultSetPanelDataContainer"})


mod_page = requests.get('https://www.pathofexile.com/trade/search/Delirium/Ab3LSL')
mod_source = mod_page.content.decode('utf-8')

soup = bs(mod_source, 'lxml')
soup.find('i', class_ = 'mutate-type mutate-type-pseudo')
soup.find_all('span')

soup.get_text

soup.find('i class')

i class="mutate-type mutate-type-pseudo"