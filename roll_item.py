# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:50:53 2020

@author: Eric

rolls item
"""
import pyautogui as gui
from checks import check_for_mod as cfm

def roll_item(mod, rolls):
    # move mouse to item location in stash tab 355, 766
    gui.moveTo(item_in_stash_coords)
    gui.PAUSE = 0.1
    
    # screenshot the stash tab with the item to be crafted
    stash_img = screenshot(stash_coords)
    
    # create a pixel map from the image
    stash_img_pixels = stash_img.load()
    
    # checks if the item has the desired mod, if not picks up the currency
    # and starts to roll the item, each time making a check for the desired
    # mod before rolling again
    if cfm(mod) > 0:
        raise Exception('This item has the desired mod.')
    else:
        # move mouse to currency item in inventory
        gui.moveTo(top_left_inventory_coords)
                    
        # pick up currency for rolling
        gui.rightClick()
        
        # move mouse to item location in stash tab 355, 766
        gui.moveTo(item_in_stash_coords)
        #gui.PAUSE = 0.1
        for k in range(rolls):
            if cfm(mod) > 0:
                raise Exception('This item has the desired mod.')
            else:
                print('roll me!')

                #shift and left click to roll
                gui.keyDown('shift')
                gui.leftClick()
        
        gui.keyUp('shift')