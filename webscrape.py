# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:13:44 2020

@author: Eric
"""
import re
#import time
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

###########################################################
# Selenium
# setup options to make chrome headless
opts = Options()
opts.headless = True

# loads the chromedriver exe which opens a chrome window
driver = webdriver.Chrome(r'C:/chromedriver/chromedriver.exe', options=opts)

# comment out three lines above if chrome needs to be run with a head
#driver = webdriver.Chrome(r'C:/chomedriver/chromedriver.exe')

# loads the URL
driver.get('https://www.pathofexile.com/trade/search/Delirium')

# convert the page to beautiful soup format
soup = bs(driver.page_source, 'html.parser')

table = soup.find_all('span', attrs={'class': 'multiselect__option'})
#table = soup.find_all('i', attrs={'class': 'mutate-type mutate-type-pseudo'})
#table = soup.find_all('i', attrs={'class': 'mutate-type mutate-type-explicit'})

mod_list = []

for span in soup.select('span'):
    mod_list.append(span.text)

# mods start at 1587 and end at 2587
#mod_list = mod_list[1587:2587]

mod_df = pd.DataFrame(data=mod_list[1587:2587])

mod_df[]

# Selenium
#####################################################
# BS
#mod_page = requests.get('https://www.pathofexile.com/trade/search/Delirium')
#mod_source = mod_page.content.decode('utf-8')
#
#soup = bs(mod_source, 'lxml')
#table = soup.find_all('i', attrs={'class': 'mutate-type mutate-type-explicit'})
#
#mod_list = []
#
#for span in soup.select('span'):
#    mod_list.append(span.text)
# BS