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
                      TOP_LEFT_CORNER, STASH_TAB_COORDS, STASH_YELLOW_TEXT,\
                      STASH_BLACK_TEXT, STASH_TAB_NAMES, \
                      LEFT_ARROW_CLICK_COORDS, YELLOW_TEXT, BLACK_TEXT,\
                      TAB_BOARDER_COORDS, TAB_CLICK_COORDS

#!!!TODO!!!
# create function that takes tab name as input. Clicks tab scroll button to
# the left and screenshots. repeats until the tab names havent changed. If tab
# not found clicks right button x times and screenshots, parses text. Continues
# until tab is found
                      
img = screenshot((220,130, 291,156))
img = color_text(img, STASH_YELLOW_TEXT, YELLOW_TEXT)
img = color_text(img, STASH_BLACK_TEXT, BLACK_TEXT)
img = image_adjustments(img)

# checks for the desired mod on the item being rolled
def check_for_text(text, coords):
    #gui.moveTo(ITEM_IN_STASH_COORDS)
    
    img = screenshot(coords)
    img = color_text(img, STASH_YELLOW_TEXT)
    img = color_text(img, STASH_BLACK_TEXT)
    img = image_adjustments(img)


img = screenshot((302,130, 362,156))
img = color_text(img, STASH_YELLOW_TEXT, YELLOW_TEXT)
img = color_text(img, STASH_BLACK_TEXT, BLACK_TEXT)
img = image_adjustments(img)

parsed_text = []
for i in range(len(TAB_BOARDER_COORDS)):
    img = screenshot(TAB_BOARDER_COORDS[i])
    img = color_text(img, STASH_YELLOW_TEXT, YELLOW_TEXT)
    img = color_text(img, STASH_BLACK_TEXT, BLACK_TEXT)
    img = image_adjustments(img)
    for j in range(len(img)):
        parsed_text.append(pytesseract.image_to_string(img[j], lang='eng', 
                                                  config = '--psm 12').lower())

parsed_text

range(3)
range(4,7)
range(8,12)
range(12,16)
range(16,20)
range(20,24)
range(24,28)

def click_on_tab(keyword):
    for i in range(4):
        if re.search(keyword, parsed_text[i]):
            print(i)
            gui.moveTo(TAB_CLICK_COORDS[0])
            break
    for i in range(4,8): 
        if re.search(keyword, parsed_text[i]):
            print(i)
            gui.moveTo(TAB_CLICK_COORDS[1])
            break
    for i in range(8,12):
        if re.search(keyword, parsed_text[i]):
            print(i)
            gui.moveTo(TAB_CLICK_COORDS[2])
            break
    for i in range(12,16):
        if re.search(keyword, parsed_text[i]):
            gui.moveTo(TAB_CLICK_COORDS[3])
            break
    for i in range(16,20):
        if re.search(keyword, parsed_text[i]):
            gui.moveTo(TAB_CLICK_COORDS[4])
            break1
    for i in range(20,24):
        if re.search(keyword, parsed_text[i]):
            gui.moveTo(TAB_CLICK_COORDS[5])
            break
    for i in range(24,28):
        if re.search(keyword, parsed_text[i]):
            gui.moveTo(TAB_CLICK_COORDS[6])
            break
 
click_on_tab('esse')

len(parsed_text)
       
for i in range(8,11):
    if re.search('esse', parsed_text[i]):
        print(i)
        gui.moveTo(TAB_CLICK_COORDS[1])
    
        print(parsed_text[8:11])
        
    
    # split on \n
    for i in range(len(parsed_text)):
        parsed_text[i] = parsed_text[i].split('\n')
     
    # remove empty strings
    for i in range(len(parsed_text)):
        parsed_text[i] = [x for x in parsed_text[i] if x != '']
        
    # split on ~
    for i in range(len(parsed_text[i])):
        for j in range(len(parsed_text[j])):
            parsed_text[i][j] = parsed_text[i][j].split(' ~ ')
            
    # unpack list of lists
    for i in range(3):
        parsed_text[i] = [x for l in parsed_text[i] for x in l]
     
        
        
        
    parsed_text[2][0]
    
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

check_for_text('dump', STASH_TAB_COORDS)


# Function that checks if the area screenshotted has grey pixels.
# grey indicates the stash cannot be scrolled any further in that direction
# 0 means grey, no scroll, 1 means brown and can be scrolled
# coords input indicates the arrow to check
def check_stash_arrows(coords):
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
    

    
    
check = check_stash_arrows(LEFT_ARROW_CLICK_COORDS)
