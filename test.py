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
#import time as t
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
# static values

# various screen coordinate
# top of screen, stash/inventory
header_coords = (0, 0, 1920, 90)

# top left inventory slot
top_left_inventory_coords = (1298, 607)

# item to be rolled in bottom middle of stash tab
item_in_stash_coords = (355, 766)

# entire stash tab
stash_coords = (15, 170, 650, 750)

# currency description box when currency in top left of inventory
currency_description_coords = (1060,410,1533,588)

# grey RGB value for a normal item
grey_value = (200, 200, 200)

# yellow RGB value for a rare item
yellow_value = (254, 254, 118)

# greyish yellow RGB values for a currency item
currency_value = ((170,158,129), (140,129,105), (150,139,113), (156,145,117))

# blue RGB values for magic a item
blue_value = ((135, 135, 254), (98, 98, 188), (99, 99, 189), (74, 73, 142),\
               (74, 74, 142), (73, 73, 141), (127, 127, 239), (81, 81, 155),\
               (98, 98, 162), (108, 108, 178), (96, 96, 182), (125, 125, 233),\
               (108, 108, 181), (97, 97, 184), (123, 123, 233),(109, 109, 207))

# create a list containing the words we're looking for in the image
header_words = ['stash','inventory']

currency_items = ['orb of alteration', 'chaos orb', 'orb of scouring', \
                  'orb of transmutation', 'regal orb']

#!!!TODO!!!
#THESE NEED TO COME IN FROM THE UI
# set desired mod and number of rolls to attempt
desired_mod = 'fire resistance'
number_of_rolls = 5

# function takes an image as an input, creates a pixel map, iterates over the
# pixels and changes any blue ones to white. Helps tesseract read the text.
def color_text(img, value):
    # create a pixel map from the image
    img_pixels = img.load()
    # loops that evaluate the stash image pixels and change any blue to white
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            for k in range(len(value)):
                # change blue pixels to white
                if img_pixels[i,j] == value[k]:
                    img_pixels[i,j] = (255, 255, 255)
    return(img)



# Takes an image as input, resize the image to 3x original size 
# converts to b/w, create enhancer, apply contrast at 3 different values, 
# output list with b/w and 3 contrast adjusted images.
def image_adjustments(img): 
    # resizes image 3x larger 
    img = img.resize(((img.size[0] * 3),(img.size[1] * 3)))
    
    # convert enlarged image to black and white
    img = img.convert(mode='L')                
    
    # setup an enhancer for the black and white image
    img_enhancer = ImageEnhance.Contrast(img)
    
    # adjust contrast on the black and white imaqge
    img_enhance_1_5 = img_enhancer.enhance(1.5)
    img_enhance_2 = img_enhancer.enhance(2)
    img_enhance_2_5 = img_enhancer.enhance(2.5)
    
    # creates a list of the four images that were created
    stash_image_list = [img, img_enhance_1_5, img_enhance_2, \
                  img_enhance_2_5]
    return(stash_image_list)

# Testing functions
#stash_img = color_text(stash_img)
#img_list = image_adjustments(header_img)

# function that takes an input, coords, and makes a screenshot based upon them.
def screenshot(coords):
    img = ImageGrab.grab(bbox = (coords))
    return(img)
    
def check_for_mod(mod):
    gui.moveTo(item_in_stash_coords)
    img = screenshot(stash_coords)
    img = color_text(img, blue_value)
    img = image_adjustments(img)
    
    parsed_text = []
    for i in range(len(img)):
        parsed_text.append(pytesseract.image_to_string(img[i], lang='eng', 
                                                  config = '--psm 12').lower())
        
    mod_found = 0
    #print(mod)
    for i in range(len(parsed_text)):      
        if bool(re.search(mod, parsed_text[i])):
            mod_found += 1

    return(mod_found)

def roll_me(mod, rolls):
    # move mouse to item location in stash tab 355, 766
    gui.moveTo(item_in_stash_coords)
    gui.PAUSE = 0.1
    
    # screenshot the stash tab with the item to be crafted
    stash_img = screenshot(stash_coords)
    
    # create a pixel map from the image
    stash_img_pixels = stash_img.load()
    
    # checks the color of the item to ensure its a magic item
    for i in range(stash_img.size[0]):
        for j in range(stash_img.size[1]):
            if stash_img_pixels[i,j] == yellow_value:
                raise Exception('This item is rare and cannot be alted. ' \
                        'Place a magic item to be crafted.')
            if stash_img_pixels[i,j] == grey_value:
                raise Exception('This item is normal and cannot be alted. ' \
                        'Place a magic item to be crafted.')
    
    for k in range(rolls):
        if check_for_mod(mod) > 0:
            raise Exception('This item has the desired mod.')
        else:
            print('roll me!')
            # move mouse to currency item in inventory
            gui.moveTo(top_left_inventory_coords)
                        
            # pick up currency for rolling
            gui.rightClick()
            
            # move mouse to item location in stash tab 355, 766
            gui.moveTo(355, 766)
            gui.PAUSE = 0.1
            
            #shift and left click to roll
            gui.keyDown('shift')
            gui.leftClick()
            
            gui.keyUp('shift')


# 1. screenshot top of screen
header_img = screenshot(header_coords)
#header_img.show()

# perform adjustments
header_img = image_adjustments(header_img)

# creates an empty list to store the parsed header text
header_text = []

# parse the headers text
for i in range(len(header_img)):
    header_text.append(pytesseract.image_to_string(header_img[i], lang='eng', 
                                                  config = '--psm 12').lower())

# 2. if inventory and stash are not open, raise error and quit
inv_found = 0
stash_found = 0
for i in range(len(header_text)):
    if bool(re.search(header_words[0], header_text[i])):
        stash_found += 1
    if bool(re.search(header_words[1], header_text[i])):
        inv_found += 1    

if inv_found < 0 & stash_found < 0:
    raise Exception('The stash and inventory are not both open. ' \
                    'Please open both and try again')

# 3. screenshot currency item description and parse
# move cursor to first item slot in inventory 1300, 615
gui.moveTo(1300, 615)

# take a screenshot of the currency item description
currency_img = screenshot(currency_description_coords)

# colors the currency image item name to white
color_text(currency_img, currency_value)

# perform adjustments
currency_img = image_adjustments(currency_img)

#inventory_img = screenshot(top_left_inventory_coords)
#inventory_img = image_adjustments(inventory_img)

# parse the image for text
currency_text = []

for i in range(len(currency_img)):
    currency_text.append(pytesseract.image_to_string(currency_img[i], \
                                                          lang='eng', config =\
                                                          '--psm 12').lower())

# creates an empty list to store the currency type found in the inventory
currency_to_roll = []

# checks the parsed text against list of item types in inventory, appends to
# currency_to_roll list 
for i in range(len(currency_text)):
    for j in range(len(currency_items)):
        if bool(re.search(currency_items[j], currency_text[i])):
            currency_to_roll.append(currency_items[j])
    
# check if the value is higher than 0, indiciating there is a currency to roll
if len(currency_to_roll) < 1:
    raise Exception('You do not have currency in your inventory.' \
                    'Place it in the top left inventory slot dummy.') 

roll_me(desired_mod, number_of_rolls)