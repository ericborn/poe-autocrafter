# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:32:31 2020

@author: Eric

Used to find a particular tab within the inventory
"""
import pyautogui as gui
import pytesseract
from checks import check_inv_stash, check_for_mod
from image_manip import color_text, image_adjustments, screenshot
from constants import LEFT_ARROW_COORDS, RIGHT_ARROW_COORDS, GREY_ARROW_COLOR,\
                      ITEM_IN_STASH_COORDS, TOP_LEFT_INVENTORY_COORDS,\
                      TOP_LEFT_CORNER, STASH_TAB_COORDS, STASH_BROWN_TEXT,\
                      STASH_BLACK_TEXT, STASH_TAB_NAMES

#!!!TODO!!!
# create function that takes tab name as input. Clicks tab scroll button to
# the left and screenshots. repeats until the tab names havent changed. If tab
# not found clicks right button x times and screenshots, parses text. Continues
# until tab is found
                      
img = screenshot(STASH_TAB_COORDS)
img = color_text(img, STASH_BROWN_TEXT)
img = color_text(img, STASH_BLACK_TEXT)
img = image_adjustments(img)

# checks for the desired mod on the item being rolled
def check_for_text(text, coords):
    #gui.moveTo(ITEM_IN_STASH_COORDS)
    
    img = screenshot(coords)
    img = color_text(img, STASH_BROWN_TEXT)
    img = color_text(img, STASH_BLACK_TEXT)
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

check_for_mod('abc')


# Function that checks if the area screenshotted has grey pixels.
# grey indicates the stash cannot be scrolled any further in that direction
# 0 means grey, no scroll, 1 means brown and can be scrolled
# coords input indicates the arrow to check
def check_stash_arrows(coords):
    
    if coords = 
    
    # moves cursor to ensure its out of screenshot area
    gui.moveTo()
    
    grey = 0

    # take screenshot based upon coords inputting
    img = screenshot(coords)
    
    # convert image to pixel map
    img_pixels = img.load()
    
    # check pixel map for gray values indicating 
    #stash cannot be scrolled that way any further
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img_pixels[i,j] == GREY_ARROW_COLOR:
                grey = 0
            else:
                grey = 1
    return(grey)
    
    

def scroll_stash(direction):
    if check_inv_stash() == 1 and check_stash_arrows(direction) == 1:
        # move mouse to arrow in stash
        gui.moveTo(direction)
        for i in range(6):
            # roll item
            gui.leftClick()
    

    
    
check = check_stash_arrows(left_arrow_coords)
