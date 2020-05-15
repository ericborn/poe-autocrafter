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
#import os
#import cv2
import pyautogui as gui
import pytesseract
import numpy as np

# set path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = \
r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

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
stash_img = ImageGrab.grab(bbox = (15, 170 , 650, 750))

# create a pixel map from the image
stash_img_pixels = stash_img.load()

blue_values = ((135, 135, 254), (98, 98, 188), (99, 99, 189), (74, 73, 142), \
               (74, 74, 142), (73, 73, 141), (127, 127, 239), (81, 81, 155), \
               (98, 98, 162), (108, 108, 178), (96, 96, 182), (125, 125, 233),\
               (108, 108, 181), (97, 97, 184), (123, 123, 233),(109, 109, 207))

for i in range(stash_img.size[0]):
    for j in range(stash_img.size[1]):
        for k in range(len(blue_values)):
            # change blue pixels to white
            if stash_img_pixels[i,j] == blue_values[k]:
                stash_img_pixels[i,j] = (255, 255, 255)
        
        
        

# used to open the image that is stored in screen_cap
#screen_cap.show()


# resizes image 3x from 635x580 to 1905x1740
stash_lrg = screen_cap.resize((1905,1740))

#larger_image.show()

## output of 3x image works fairly well when converting to black and white
## correct text capture is ~90%
#parsed_lrg_img = pytesseract.image_to_string(
#                cv2.cvtColor(np.array(larger_image), cv2.COLOR_BGR2GRAY),  
#                lang ='eng') 
#print(parsed_lrg_img)
#
## creates a contrast enhancer for the larger_image
#color_enhancer = ImageEnhance.Contrast(larger_image)
#
## setting factor greater than 1 increases contrast
#enhance_output_1_5 = color_enhancer.enhance(1.5)
#enhance_output_2 = color_enhancer.enhance(2)
#enhance_output_2_5 = color_enhancer.enhance(2.5)
#
## output contrast adjusted images
#enhance_output_1_5.show()
#enhance_output_2.show()
#enhance_output_2_5.show()
#
## Parse text of contrast adjusted large image. Image being converted to 
## grayscale with cv2 prior to parse. Contrast value of of 2 performs the best 
## of the three and slighty better than previous test with no constrast 
## adjustments.
#parsed_enhanced_img = pytesseract.image_to_string(
#                cv2.cvtColor(np.array(enhance_output_2), cv2.COLOR_BGR2GRAY),  
#                lang ='eng') 
#print(parsed_enhanced_img)

# convert enlarged image to black and white
stash_bw = stash_lrg.convert(mode='L')
#bw_img.show()

# Parse image converted to black and white using PIL. 
# Great results ~99% captured, slightly better than an contrast images being
# converted to grayscale by cv2
#parsed_bw_img = pytesseract.image_to_string(bw_img,  
#                lang ='eng') 
#print('!!!parsed_bw_img!!!\n' + parsed_bw_img)

# setup an enhancer for the black and white image
stash_enhancer = ImageEnhance.Contrast(stash_bw)

# adjust contrast on the black and white imaqge
stash_enhance_blk_1_5 = stash_enhancer.enhance(1.5)
stash_enhance_blk_2 = stash_enhancer.enhance(2)
stash_enhance_blk_2_5 = stash_enhancer.enhance(2.5)

#enhance_blk_1_5.show()
#enhance_blk_2.show()
#enhance_blk_2_5.show()

# Parse using black and white image with contrast adjusted.
# 1.5 performs the best and is very comparable to non-adjusted black and white.
# This parse picked up the title of the item but droped the letters INT in the
# item requirement section, where the parsed_bw_img performed opposite.
# both missed the value preceding the INT requirement due to the text being red
# in color
#parsed_enhance_blk_1_5 = pytesseract.image_to_string(enhance_blk_1_5,  
#                lang ='eng') 
#print('!!!parsed_enhance_blk_1_5!!!\n' + parsed_enhance_blk_1_5)
#
#parsed_enhance_blk_2 = pytesseract.image_to_string(enhance_blk_2,  
#                lang ='eng') 
#print('!!!parsed_enhance_blk_2!!!\n' + parsed_enhance_blk_2)
#
#parsed_enhance_blk_2_5 = pytesseract.image_to_string(enhance_blk_2_5,  
#                lang ='eng') 
#print('!!!parsed_enhance_blk_2_5!!!\n' + parsed_enhance_blk_2_5)

# creates a list of the four images that were created
stash_image_list = [stash_bw, stash_enhance_blk_1_5, stash_enhance_blk_2, \
              stash_enhance_blk_2_5]

# create a list which will contain the text from each parsed image
parsed_list = []

for i in range(len(stash_image_list)):
    parsed_list.append(pytesseract.image_to_string(stash_image_list[i]).lower(),
                       lang='eng')

keyword = 'evasion rating'



'''
1. screenshot top of screen
2. if inventory and stash not open, raise error and quit
3. screenshot inventory and parse
5. if no alts present, raise error and quit
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

header_img = ImageGrab.grab(bbox = (0, 0 , 1920, 90))
header_img.show()

header_text = pytesseract.image_to_string(header_img)

# resizes image 3x from 635x580 to 1905x1740
stash_lrg = screen_cap.resize((1905,1740))

# item location in stash tab 355, 766
# first item slot in inventory 1300, 615

gui.moveTo(355, 766)

def useAlteration(self):
    

for i in range(len(parsed_list)):  
    found = 0
    if bool(re.search(keyword, parsed_list[i])):
        found += 1
        print('found')
    else:
        print('not found')
    if found == 0:
        
        

