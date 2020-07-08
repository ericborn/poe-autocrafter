# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:50:53 2020

@author: Eric

rolls item
"""
import pyautogui as gui
from constants import ITEM_IN_STASH_COORDS, INVENTORY_X_COORDS, \
                      INVENTORY_Y_COORDS

#def unstack_and_move(item_type, number, x, y):
#    gui.moveTo(INVENTORY_X_COORDS[x], INVENTORY_Y_COORDS[y])
#    gui.leftClick()
#    gui.keyUp('shift')

def roll_item(x, y):
    # move mouse to currency item in inventory
    gui.moveTo(INVENTORY_X_COORDS[x], INVENTORY_Y_COORDS[y])
                    
    # pick up currency for rolling
    gui.rightClick()
    
    # move mouse to item location in stash tab 355, 766
    gui.moveTo(ITEM_IN_STASH_COORDS)
    
    # roll item
    gui.leftClick()