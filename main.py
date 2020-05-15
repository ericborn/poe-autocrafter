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
import os
import cv2
import pytesseract
import numpy as np

# set path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = \
r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# stores an image of the entire normal stash tab
# width x height
# 635x580 original
# 1905x1740 x3 size
screen_cap = ImageGrab.grab(bbox = (15, 170 , 650, 750))

# create a pixel map from the image
screen_cap_pixels = screen_cap.load()

for i in range(bw_img.size[1])

# resizes image 3x from 635x580 to 1905x1740
larger_image = screen_cap.resize((1905,1740))

# used to display the image that is stored in larger_image
#larger_image.show()

# convert enlarged image to black and white
bw_img = larger_image.convert(mode='L')
#bw_img.show()

# Parse image converted to black and white using PIL. 
# Great results ~99% captured, slightly better than an contrast images being
# converted to grayscale by cv2
parsed_bw_img = pytesseract.image_to_string(bw_img,  
                lang ='eng')
print(parsed_bw_img)

# setup an enhancer for the black and white image
bw_enhancer = ImageEnhance.Contrast(bw_img)

# adjust contrast on the black and white imaqge
enhance_blk_1_5 = bw_enhancer.enhance(1.5)
enhance_blk_2 = bw_enhancer.enhance(2)
enhance_blk_2_5 = bw_enhancer.enhance(2.5)

#enhance_blk_1_5.show()
#enhance_blk_2.show()
#enhance_blk_2_5.show()

# Parse using black and white image with contrast adjusted.
# 1.5 performs the best and is very comparable to non-adjusted black and white.
# This parse picked up the title of the item but droped the letters INT in the
# item requirement section, where the parsed_bw_img performed opposite.
# both missed the value preceding the INT requirement due to the text being red
# in color
parsed_lrg_img = pytesseract.image_to_string(enhance_blk_1_5,  
                #lang ='eng')
                lang ='eng', config='--psm 11')
print(parsed_lrg_img)

#blue
#135, 135, 254
#98, 98, 188

#!!!! TODO
# Test sampling text colors, blue, grey, yellow, red, white
# and convert all colors to white