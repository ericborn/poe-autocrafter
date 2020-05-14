# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:38:23 2020

@author: Eric
"""
from PIL import Image
import os
#import io
import pytesseract

# setup file location
path = r'C:\Code projects\git projects\poe-autocrafter\images'
file = 'stash1'
full_path = os.path.join(path, file + '.png')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

text = pytesseract.image_to_string(full_path, lang = 'eng')

print(text)