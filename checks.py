# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:29:30 2020

@author: Eric

Checks for the item being crafted for mod thats being input into the function 
by moving the mouse over it, taking a screenshot, coloring the blue text to 
white, performing image adjustments, parsing text and checking that for the
desired mod words.
"""
import pyautogui as gui
import pytesseract
import re
from image_manip import color_text, image_adjustments, screenshot

# static values
# various screen coordinate
# top of screen, stash/inventory
header_coords = (0, 0, 1920, 90)

# item to be rolled in bottom middle of stash tab
item_in_stash_coords = (355, 766)

# entire stash tab
stash_coords = (15, 170, 650, 750)

# top left inventory slot
top_left_inventory_coords = (1300, 610)

# currency description box when currency in top left of inventory
currency_description_coords = (1060,410,1533,588)

# blue RGB values for magic a item
blue_value = ((135, 135, 254), (98, 98, 188), (99, 99, 189), (74, 73, 142),\
               (74, 74, 142), (73, 73, 141), (127, 127, 239), (81, 81, 155),\
               (98, 98, 162), (108, 108, 178), (96, 96, 182), (125, 125, 233),\
               (108, 108, 181), (97, 97, 184), (123, 123, 233),(109, 109, 207))

# grey RGB value for a normal item
grey_value = (200, 200, 200)

# yellow RGB value for a rare item
yellow_value = (254, 254, 118)

# greyish yellow RGB values for a currency item
currency_value = ((170,158,129), (140,129,105), (150,139,113), (156,145,117))

# create a list containing the words we're looking for in the image
currency_items = ['orb of alteration', 'chaos orb', 'orb of scouring', \
                  'orb of transmutation', 'regal orb']

# create a list containing the words we're looking for in the image
header_words = ['stash','inventory']

# checks for the stash and invetory to be open
def inv_stash_check():
    # Screenshot top of screen
    header_img = screenshot(header_coords)
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
        if bool(re.search(header_words[0], header_text[i])):
            stash_found += 1
        if bool(re.search(header_words[1], header_text[i])):
            inv_found += 1    
    
    if inv_found < 1 or stash_found < 1:
        return(-1)
        print('The stash and inventory are not both open. '\
              'Please open both and try again')
    if inv_found > 0 and stash_found > 0:
        return(1)
        print('The stash and inventory are both open.')

def check_for_magic():
    gui.moveTo(item_in_stash_coords)
    img = screenshot(stash_coords)
        
    # create a pixel map from the image
    img_pixels = img.load()
    
    # checks the color of the item to ensure its a magic item
    for i in range(img.size[0]):
        for j in range(img.size[1]):
#            if img_pixels[i,j] == yellow_value:
#                raise Exception('This item is rare and cannot be alted. ' \
#                        'Place a magic item to be crafted.')
#            if img_pixels[i,j] == grey_value:
#                raise Exception('This item is normal and cannot be alted. ' \
#                        'Place a magic item to be crafted.')
            if img_pixels[i,j] == yellow_value:
                return(-1)
                print('This item is rare and cannot be alted.'\
                        'Place a magic item to be crafted.')
            elif img_pixels[i,j] == grey_value:
                return(-1) 
                print('This item is normal and cannot be alted.'\
                        ' Place a magic item to be crafted.')
            else:
                return(1, 'Item is magic, roll it')


# screenshot currency item description and parse
def check_for_currency():
    # move cursor to first item slot in inventory 1300, 615
    gui.moveTo(top_left_inventory_coords)
    
    # take a screenshot of the currency item description
    img = screenshot(currency_description_coords)
    
    # colors the currency image item name to white
    color_text(img, currency_value)
    
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
        for j in range(len(currency_items)):
            if bool(re.search(currency_items[j], currency_text[i])):
                currency_to_roll.append(currency_items[j])
    
    # check if the value is higher than 0, indiciating there is a currency to roll
    if len(currency_to_roll) < 1:
        return(-1)
        print('You do not have currency in your inventory.' \
              'Place it in the top left inventory slot dummy.')
    else:
        return(1)
    
 # checks for the desired mod on the item being rolled
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
    if mod_found <= 0:
        return(-1,)
    else:
        return(1)   
