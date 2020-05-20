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

# blue RGB values for magic a item
blue_value = ((135, 135, 254), (98, 98, 188), (99, 99, 189), (74, 73, 142),\
               (74, 74, 142), (73, 73, 141), (127, 127, 239), (81, 81, 155),\
               (98, 98, 162), (108, 108, 178), (96, 96, 182), (125, 125, 233),\
               (108, 108, 181), (97, 97, 184), (123, 123, 233),(109, 109, 207))

# create a list containing the words we're looking for in the image
header_words = ['stash','inventory']

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

    return(mod_found)
    
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
        return(-1, 'The stash and inventory are not both open. ', 
                        'Please open both and try again')
    if inv_found > 0 and stash_found > 0:
        return(1, 'The stash and inventory are both open.')