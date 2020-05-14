# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:38:23 2020

Program is written to read the screen while playing the game Path of Exile
Automatically crafts an item looking for specific mods and stops once the mods
have been achieved

@author: Eric

Game played on windowed fullscreen at 1920x1080
Coordinates to look within for text

top left inventory
(1000, 175, 1600, 640)

bottom right inventory
(1360, 500, 1920, 830)

bottom middle of stash tab
(30, 400 , 580, 750)

testing at windowed 800x600, game in top left corner produced worse results
(10, 270, 320, 445)
"""
from PIL import Image, ImageGrab, ImageEnhance
import os
import cv2
import pytesseract
import numpy as np

# set path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Manual test for a static image
# setup file location
#path = r'C:\Code projects\git projects\poe-autocrafter\images'
#file = 'stash1'
#full_path = os.path.join(path, file + '.png')

# uses pytess image to string pulling from the image with 
# language set to english
#text = pytesseract.image_to_string(full_path, lang = 'eng')

#print(text)

# magic map test in empty stash tab
# width x height
# 550x350 original
# 1650x1050 x3 size
#screen_cap = ImageGrab.grab(bbox = (30, 400 , 580, 750))

# used to open the image that is stored in screen_cap
#screen_cap.show()

# resizes image 3x from 550x300 to 1650x1050
#larger_image = screen_cap.resize((1650,1050))

# save image to file
#larger_image.save('test1.png')

#tesstr = pytesseract.image_to_string(larger_image,
                #cv2.cvtColor(np.array(larger_image), cv2.COLOR_BGR2GRAY),  
#                lang ='eng') 
#print(tesstr)

# rare boots test in empty stash tab
# width x height of an entire normal stash tab
# 635x580 original
# 1905x1740 x3 size
screen_cap = ImageGrab.grab(bbox = (15, 170 , 650, 750))

# used to open the image that is stored in screen_cap
#screen_cap.show()

# resizes image 3x from 635x580 to 1905x1740
larger_image = screen_cap.resize((1905,1740))

larger_image.show()

# output of 3x image works fairly well when converting to black and white
# correct text capture is ~90-95%
parsed_lrg_img = pytesseract.image_to_string(
                cv2.cvtColor(np.array(larger_image), cv2.COLOR_BGR2GRAY),  
                lang ='eng') 
print(tesstr)

# creates a contrast enhancer for the larger_image
enhancer = ImageEnhance.Contrast(larger_image)

# setting factor greater than 1 increases contrast
factor = 2

enhance_output = enhancer.enhance(factor)

enhance_output.show()

# save image to file
#larger_image.save('test1.png')

