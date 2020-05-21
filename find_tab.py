# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:32:31 2020

@author: Eric

Used to find a particular tab within the inventory
"""
from image_manip import color_text, image_adjustments, screenshot
from constants import LEFT_ARROW_COORDS, RIGHT_ARROW_COORDS, GREY_ARROW_COLOR,\
                      ITEM_IN_STASH_COORDS, TOP_LEFT_INVENTORY_COORDS
import pyautogui as gui

#!!!TODO!!!
# create function that takes tab name as input. Clicks tab scroll button to
# the left and screenshots. repeats until the tab names havent changed. If tab
# not found clicks right button x times and screenshots, parses text. Continues
# until tab is found

#!!!TODO!!!
#CHECKING FOR BOTH ARROWS BEING BROWN, DOES IT MATTER OR JUST SCROLL LEFT 
#UNTIL GREY THEN START SCANNING FOR DESIRED TABS?


# creates a function that checks if the area screenshotted has grey pixels
# grey indicates the stash cannot be scrolled any further in that direction
# 0 means grey, no scroll, 1 means brown and can be scrolled
def check_stash_arrows(coords):
    grey = 0
    #right = 0
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
    
    

                    
    # pick up currency for rolling
    gui.rightClick()
    
    # move mouse to item location in stash tab 355, 766
    gui.moveTo(ITEM_IN_STASH_COORDS)
    
    # roll item
    gui.leftClick()

def click_arrow(direction):
    # move mouse to arrow in stash
    gui.moveTo(TOP_LEFT_INVENTORY_COORDS)
    
    
    
    
    
check = check_stash_arrows(left_arrow_coords)
