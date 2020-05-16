# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:38:23 2020

Program is written to read the screen while playing the game Path of Exile
Automatically crafts an item looking for specific mods and stops once the mods
have been achieved

@author: Eric

Game played on windowed fullscreen at 1920x1080
Coordinates for an empty stash tab to look within for text
(15, 170 , 650, 750)

testing at windowed 800x600, game in top left corner produced worse results

Scaling image by 3x produces much better results than the native resolution

Enhancing contrast by 2 also improves parsing results, 1.5 and 2.5 produce
worse results

"""
from PIL import Image, ImageGrab, ImageEnhance
import re
import time as t
#import os
#import cv2
import pyautogui as gui
import pytesseract
import numpy as np

# set path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = \
r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

'''
6. screen stash and parse
7. if item has mod desired, raise error and quit
8. move mouse to 1st alt location
9. right click
10. move mouse to item location
11. hold shift and left click
12. screenshot stash and parse
13. if item has desired mod, return success and quit
14. if item does not have desired mod, return to step 11, 
    repeat number of requested times
    
inventory slots
1270x585
1910x860

top header for stash and inventory text
0x0
1920x90
'''

# 1. screenshot top of screen
header_img = ImageGrab.grab(bbox = (0, 0, 1920, 90))
#header_img.show()

# resizes image 3x from 635x580 to 5760x270
header_img = header_img.resize((5760,270))
#header_lrg.show()

# convert enlarged image to black and white
header_img = header_img.convert(mode='L')
#header_bw.show()

# setup an enhancer for the black and white image
header_enhancer = ImageEnhance.Contrast(header_img)

# adjust contrast on the black and white imaqge
header_img = header_enhancer.enhance(1.5)
#header_enhance_blk_1_5.show()

# parse the headers text
header_text = pytesseract.image_to_string(header_img, lang='eng', 
                                          config = '--psm 12').lower()
# create list containing the words we're looking for in the image
header_words = ['stash','inventory']

# 2. if inventory and stash are not open, raise error and quit
header_found = 0
for i in range(len(header_words)):
    if bool(re.search(header_words[i], header_text)):
        header_found += 1

if header_found < 2:
    raise Exception('The stash and inventory are not both open. ' \
                    'Please open both and try again') 

# 3. screenshot top left corner of inventory and parse
inventory_img = ImageGrab.grab(bbox = (1270, 585, 1298, 607))

# convert enlarged image to black and white
inventory_img = inventory_img.convert(mode='L')

# setup an enhancer for the black and white image
inventory_enhancer = ImageEnhance.Contrast(inventory_img)

# adjust contrast on the black and white imaqge
inventory_img = inventory_enhancer.enhance(1.5)

#inventory_img.show()

    # parse the image and convert the output to an int
try:
    currency_count = int(pytesseract.image_to_string(inventory_img, lang='eng', 
                                                   config = '--psm 6').lower())
except Exception as e:
    print(e)
    exit('You do not have currency in your inventory.')
    
# check if the value is higher than 0
if currency_count < 1:
    raise Exception('You do not have currency in your inventory.' \
                    'Place it in the top left inventory slot dummy.') 


# move mouse to item location in stash tab 355, 766
gui.moveTo(355, 766)

t.sleep(1)

# width x height of an entire normal stash tab
# 635x580 original
# 1905x1740 x3 size
stash_img = ImageGrab.grab(bbox = (15, 170, 650, 750))

# create a pixel map from the image
stash_img_pixels = stash_img.load()

# store the grey RGB value indicating its a rare item
grey_value = (200, 200, 200)

# store the yellow RGB value indicating its a rare item
yellow_value = (254, 254, 118)

# store blue RGB values
blue_values = ((135, 135, 254), (98, 98, 188), (99, 99, 189), (74, 73, 142), \
               (74, 74, 142), (73, 73, 141), (127, 127, 239), (81, 81, 155), \
               (98, 98, 162), (108, 108, 178), (96, 96, 182), (125, 125, 233),\
               (108, 108, 181), (97, 97, 184), (123, 123, 233),(109, 109, 207))

for i in range(stash_img.size[0]):
    for j in range(stash_img.size[1]):
        if stash_img_pixels[i,j] == yellow_value:
            raise Exception('This item is rare and cannot be alted. ' \
                    'Place a magic item to be crafted.')
        if stash_img_pixels[i,j] == grey_value:
            raise Exception('This item is normal and cannot be alted. ' \
                    'Place a magic item to be crafted.')

# loops that evaluate the stash image pixels and change any blue to white
for i in range(stash_img.size[0]):
    for j in range(stash_img.size[1]):
        for k in range(len(blue_values)):
            # change blue pixels to white
            if stash_img_pixels[i,j] == blue_values[k]:
                stash_img_pixels[i,j] = (255, 255, 255)