"""
Created on Mon May 18 12:32:31 2020

@author: Eric

Used to find a particular tab within the inventory
"""
import sys
import time as t
sys.path.append(r'C:\Code projects\git projects\poe-autocrafter')
import pyautogui as gui
from constants import SORT_SEARCH_NAMES, TAB_CLICK_COORDS, \
                      RIGHT_ARROW_CLICK_COORDS, LEFT_ARROW_CLICK_COORDS
from find_tab import search_and_move, move_to_stash

def sort_inventory():
    for i in range(len(SORT_SEARCH_NAMES)):
        items = search_and_move(SORT_SEARCH_NAMES[i])
        
        # click on tab, put items, click back on dump
        if items > 0 and i <= 5:
            
            # move mouse to tab and click then put items
            gui.moveTo(TAB_CLICK_COORDS[i + 1])
            t.sleep(0.1)
            gui.leftClick()
            move_to_stash(items)
            t.sleep(0.1)
            
            # move back to dump tab and click
            gui.moveTo(TAB_CLICK_COORDS[0])
            t.sleep(0.1)
            gui.leftClick()
            
        # click scroll x times, click on tab, put items, scroll back, click on dump
        elif items > 0 and i >= 6 and i <= 8:
            for j in range(i-5):
                # scroll stash right
                gui.moveTo(RIGHT_ARROW_CLICK_COORDS)
                t.sleep(0.1)
                gui.leftClick()
            
            # move mouse to tab and click then put items
            gui.moveTo(TAB_CLICK_COORDS[6])
            t.sleep(0.1)
            gui.leftClick()
            move_to_stash(items)
            
            # move back to dump tab and click
            for k in range(i-5):
                # scroll stash left
                gui.moveTo(LEFT_ARROW_CLICK_COORDS)
                t.sleep(0.1)
                gui.leftClick()
                
            # move back to dump tab and click
            gui.moveTo(TAB_CLICK_COORDS[0])
            t.sleep(0.1)
            gui.leftClick()
        
        # separate statement that handles non 1x1 items
        elif items > 0 and i == 9:
            for j in range(i-5):
                # scroll stash right
                gui.moveTo(RIGHT_ARROW_CLICK_COORDS)
                t.sleep(0.1)
                gui.leftClick()
                
            # move mouse to tab and click then put items
            gui.moveTo(TAB_CLICK_COORDS[6])
            t.sleep(0.1)
            gui.leftClick()
            items *= 4
            move_to_stash(items)
            
            # move back to dump tab and click
            for k in range(i-5):
                # scroll stash left
                gui.moveTo(LEFT_ARROW_CLICK_COORDS)
                t.sleep(0.1)
                gui.leftClick()
            
            # move back to dump tab and click
            gui.moveTo(TAB_CLICK_COORDS[0])
            t.sleep(0.1)
            gui.leftClick()
            
         # click scroll x times, click on tab, put items, scroll back, click on dump
        elif items > 0 and i >= 10:
            for j in range(i-5):
                # scroll stash right
                gui.moveTo(RIGHT_ARROW_CLICK_COORDS)
                t.sleep(0.1)
                gui.leftClick()
            
            # move mouse to tab and click then put items
            gui.moveTo(TAB_CLICK_COORDS[6])
            t.sleep(0.1)
            gui.leftClick()
            move_to_stash(items)
            
            # move back to dump tab and click
            for k in range(i-5):
                # scroll stash left
                gui.moveTo(LEFT_ARROW_CLICK_COORDS)
                t.sleep(0.1)
                gui.leftClick()
            
            # move back to dump tab and click
            gui.moveTo(TAB_CLICK_COORDS[0])
            t.sleep(0.1)
            gui.leftClick()