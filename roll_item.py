# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:50:53 2020

@author: Eric

rolls item
"""
import pyautogui as gui
from constants import ITEM_IN_STASH_COORDS

def roll_item(coords):
    # move mouse to currency item in inventory
    gui.moveTo(coords)
                    
    # pick up currency for rolling
    gui.rightClick()
    
    # move mouse to item location in stash tab 355, 766
    gui.moveTo(ITEM_IN_STASH_COORDS)
    
    # roll item
    gui.leftClick()