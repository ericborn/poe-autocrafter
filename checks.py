# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:29:30 2020

@author: Eric

Checks for the item being crafted for mod thats being input into the function 
by moving the mouse over it, taking a screenshot, coloring the blue text to 
white, performing image adjustments, parsing text and checking that for the
desired mod words.
"""
import re
import time as t
import pytesseract
import pyautogui as gui
from image_manip import color_text, image_adjustments, screenshot
from constants import HEADER_COORDS, ITEM_IN_STASH_COORDS, \
                      ENTIRE_STASH_COORDS, TOP_LEFT_INVENTORY_COORDS, \
                      CURRENCY_DESCRIPTION_COORDS, BLUE_COLOR, \
                      GREY_ITEM_COLOR, YELLOW_ITEM_COLOR, \
                      CURRENCY_ITEM_COLOR, CURRENCY_NAMES, HEADER_WORDS




# checks for the stash and invetory to be open
def check_inv_stash():
    # Screenshot top of screen
    header_img = screenshot(HEADER_COORDS)
    #header_img.show()

    # Perform adjustments
    header_img = image_adjustments(header_img)

    # Creates an empty list to store the parsed header text
    header_text = []

    # Parse the headers text
    for i in range(len(header_img)):
        header_text.append(pytesseract.image_to_string(header_img[i], 
                                                       lang='eng', 
                                                       config = '--psm 12')\
                                                       .lower())

    # If inventory and stash are not open, raise error and quit
    inv_found = 0
    stash_found = 0
    for i in range(len(header_text)):
        if bool(re.search(HEADER_WORDS[0], header_text[i])):
            stash_found += 1
        if bool(re.search(HEADER_WORDS[1], header_text[i])):
            inv_found += 1    
    
    if inv_found < 1 or stash_found < 1:
        return(-1)
        print('The stash and inventory are not both open. '\
              'Please open both and try again')
    if inv_found > 0 and stash_found > 0:
        return(1)
        print('The stash and inventory are both open.')

def check_for_magic():
    # move to item coords in stash
    gui.moveTo(ITEM_IN_STASH_COORDS)
    
    # sleep 0.1 second to allow item text to appear
    t.sleep(0.1)
    
    # take screenshot
    img = screenshot(ENTIRE_STASH_COORDS)
        
    # create a pixel map from the image
    img_pixels = img.load()
    
    yellow_count = 0
    grey_count = 0
    blue_count = 0
    # checks the color of the item to ensure its a magic item
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img_pixels[i,j] == YELLOW_ITEM_COLOR:
                yellow_count += 1

            if img_pixels[i,j] == GREY_ITEM_COLOR:
                grey_count += 1

            if img_pixels[i,j] == BLUE_COLOR[1]:
                blue_count += 1

    # checks color counts to determine item rarity
    if grey_count > 10:
        return(-1) 
        print('This item is normal and cannot be alted.'\
              ' Place a magic item to be crafted.')
    elif yellow_count > 10:
        return(-1) 
        print('This item is rare and cannot be alted.'\
              ' Place a magic item to be crafted.')
    elif yellow_count == 0 and blue_count > 10:
        return(1) 
        print('This item is magic and can be alted.')

# screenshot currency item description and parse
def check_for_currency():
    # move cursor to first item slot in inventory 1300, 615
    gui.moveTo(TOP_LEFT_INVENTORY_COORDS)
    
    # sleep 0.1 second to allow item text to appear
    t.sleep(0.1)
   
    # take a screenshot of the currency item description
    img = screenshot(CURRENCY_DESCRIPTION_COORDS)
    
    # colors the currency image item name to white
    color_text(img, CURRENCY_ITEM_COLOR)
    
    # perform adjustments
    img = image_adjustments(img)
    
    #inventory_img = screenshot(top_left_inventory_coords)
    #inventory_img = image_adjustments(inventory_img)
    
    # parse the image for text
    currency_text = []
    
    for i in range(len(img)):
        currency_text.append(pytesseract.image_to_string(img[i], lang='eng', \
                                                         config = '--psm 12')\
                                                        .lower())
    
    # creates an empty list to store the currency type found in the inventory
    currency_to_roll = []
    
    # checks the parsed text against list of item types in inventory, appends to
    # currency_to_roll list 
    for i in range(len(currency_text)):
        for j in range(len(CURRENCY_NAMES)):
            if bool(re.search(CURRENCY_NAMES[j], currency_text[i])):
                currency_to_roll.append(CURRENCY_NAMES[j])
    
    # check if the value is higher than 0, indiciating there is a currency to roll
    if len(currency_to_roll) < 1:
        return(-1)
        print('You do not have currency in your inventory.' \
              'Place it in the top left inventory slot dummy.')
    else:
        return(1)
    
# checks for the desired mod on the item being rolled
def check_for_mod(mod):
    gui.moveTo(ITEM_IN_STASH_COORDS)
    
    # sleep 0.1 second to allow item text to appear
    t.sleep(0.1)

    img = screenshot(ENTIRE_STASH_COORDS)
    img = color_text(img, BLUE_COLOR)
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
    # if mod found is greater than 0, mod is found so return -1 to stop rolling
    # mod found = 0, return 1 which indicates continue to roll
    if mod_found > 0:
        return(-1)
    else:
        return(1)   
