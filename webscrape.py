# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:13:44 2020

@author: Eric
"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import time

mod_page = requests.get('https://www.pathofexile.com/trade/search/Delirium/Ab3LSL')
mod_source = mod_page.content.decode('utf-8')

soup = bs(mod_source, 'lxml')
soup.find('i', class_ = 'mutate-type mutate-type-pseudo')
soup.find_all('span')

soup.get_text

soup.find('i class')

i class="mutate-type mutate-type-pseudo"