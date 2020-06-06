# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:32:31 2020

@author: Eric

Used to find a particular tab within the inventory
"""
import sys
sys.path.append(r'C:\Code projects\git projects\poe-autocrafter')
import re
import time as t
import math as m
import pyautogui as gui
import pytesseract
import numpy as np
from checks import check_inv_stash, check_for_mod
from image_manip import color_text, image_adjustments, screenshot
from constants import LEFT_ARROW_COORDS, RIGHT_ARROW_COORDS, GREY_ARROW_COLOR,\
                      ITEM_IN_STASH_COORDS, TOP_LEFT_INVENTORY_COORDS,\
                      TOP_LEFT_CORNER, STASH_TAB_COORDS, STASH_YELLOW_TEXT,\
                      STASH_BLACK_TEXT, STASH_TAB_NAMES, BLACK_TEXT,\
                      LEFT_ARROW_CLICK_COORDS, YELLOW_TEXT, TAB_CLICK_COORDS,\
                      TAB_BOARDER_COORDS, RIGHT_ARROW_CLICK_COORDS,\
                      STASH_SEARCH_BOX, SORT_SEARCH_NAMES, YELLOW_BORDER,\
                      ENTIRE_STASH_COORDS, INVENTORY_Y_COORDS, \
                      INVENTORY_X_COORDS, EQUIPMENT_SORTING_INDEX

def check_stash_tabs():
    gui.moveTo(TOP_LEFT_CORNER)
    parsed_text = []
    for i in range(len(TAB_BOARDER_COORDS)):
        img = screenshot(TAB_BOARDER_COORDS[i])
        img = color_text(img, STASH_YELLOW_TEXT, YELLOW_TEXT)
        img = color_text(img, STASH_BLACK_TEXT, BLACK_TEXT)
        img = image_adjustments(img)
        for j in range(len(img)):
            parsed_text.append(pytesseract.image_to_string(img[j], lang='eng', 
                                                      config = '--psm 12').lower())
    return(parsed_text)

def check_for_text(text, coords):
    gui.moveTo(TOP_LEFT_CORNER)
    
    img = screenshot(coords)
    img = color_text(img, STASH_BLACK_TEXT, BLACK_TEXT)
    img = color_text(img, STASH_YELLOW_TEXT, YELLOW_TEXT)
    img = image_adjustments(img)
    
    parsed_text = []
    for i in range(len(img)):
        parsed_text.append(pytesseract.image_to_string(img[i], lang='eng', 
                                                  config = '--psm 12').lower())
        
    text_found = 0
    #print(mod)
    for i in range(len(parsed_text)):      
        if bool(re.search(text, parsed_text[i])):
            text_found += 1
    # if mod found is greater than 0, mod is found so return -1 to stop rolling
    # mod found = 0, return 1 which indicates continue to roll
    if text_found > 0:
        return(-1)
    else:
        return(1) 

#!!!TODO!!!
# FIND A WAY TO CLICK LEFT/RIGHT IF THE WORD ISNT FOUND
def click_on_tab(keyword):
    # takes a screenshot of the stash area, parses text and stores it as a list
    stash_text = check_stash_tabs()
    
    # loops through the parsed text and depending on where its found
    # clicks on the appropriate tab
    click_check = 0
    for i in range(28):
        if re.search(keyword, stash_text[i]) and i <= 3:
            gui.leftClick(TAB_CLICK_COORDS[0])
            click_check += 1
            return(click_check)
        elif re.search(keyword, stash_text[i]) and 4 <= i <= 7:
            gui.leftClick(TAB_CLICK_COORDS[1])
            click_check += 1
            return(click_check)
        elif re.search(keyword, stash_text[i]) and 8 <= i <= 11:
            gui.leftClick(TAB_CLICK_COORDS[2])
            click_check += 1
            return(click_check)
        elif re.search(keyword, stash_text[i]) and 12 <= i <= 15:
            gui.leftClick(TAB_CLICK_COORDS[3])
            click_check += 1
            return(click_check)
        elif re.search(keyword, stash_text[i]) and 16 <= i <= 19:
            gui.leftClick(TAB_CLICK_COORDS[4])
            click_check += 1
            return(click_check)
        elif re.search(keyword, stash_text[i]) and 20 <= i <= 23:
            gui.leftClick(TAB_CLICK_COORDS[5])
            click_check += 1
            return(click_check)
        elif re.search(keyword, stash_text[i]) and 24 <= i <= 27:
            gui.leftClick(TAB_CLICK_COORDS[6])
            click_check += 1
            return(click_check)
    return(click_check)

def item_to_inventory():
    gui.keyDown('ctrl')
    gui.leftClick()
    gui.keyUp('ctrl')

# moves to search box location, clicks to start the cursor, 
# types the search word
def stash_search(keyword):
    gui.moveTo(STASH_SEARCH_BOX)
    gui.leftClick()
    gui.hotkey('ctrl', 'a')
    gui.hotkey('backspace')
    gui.typewrite(keyword)
    
# Function that checks if the area screenshotted has grey pixels.
# grey indicates the stash cannot be scrolled any further in that direction
# 0 means grey, no scroll, 1 means brown and can be scrolled
# coords input indicates the arrow to check
def check_stash_arrows(coords):
    # moves cursor to ensure its out of screenshot area
    gui.moveTo(TOP_LEFT_CORNER)
    
    # indicator for the arrow being grey or not
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
                grey += 1
                return(grey)
    return(grey)
    
def click_stash_arrow(direction):
    # move mouse to arrow in stash
    gui.moveTo(direction)
    for i in range(7):
        # left click
        gui.leftClick()

def scroll_stash(stash_tab_name):
    # if the click_on_tab returns 0, the tab name wasnt found
    # check to see if the left scroll arrow is grey, if it is, scroll right
    number_of_scrolls = 0
    for i in range(6):
        tab_check = click_on_tab(stash_tab_name)
    
        if tab_check == 0:
            #if check_stash_arrows(LEFT_ARROW_COORDS) > 0:
            click_stash_arrow(RIGHT_ARROW_CLICK_COORDS)
            number_of_scrolls += 1
        else:
            print('found it')
            gui.leftClick()
            return(number_of_scrolls)

def scan_pixels(img):
    for k in range(img.size[0]):
        for l in range(img.size[1]):
            r, g, b = img.getpixel((k, l))
            if img.getpixel((k, l)) == YELLOW_BORDER:
                #print(f"Found yellow at {k},{l}!")
                return([k,l])         
    return(0)

def move_from_stash():
    # total_items moved into the inventory
    total_items = 0
    
    for i in range(60):
    
        # screenshot the stash
        img = screenshot(ENTIRE_STASH_COORDS)

        # create empty list to store item yellow border coordinates
        pixel_coord = scan_pixels(img)

        # pixels are offset by 25/170 because the screenshot does not start at
        # (0, 0) but (12, 162)
        if pixel_coord == 0:
            print('none found')
            return(total_items)
        else:
            gui.moveTo([pixel_coord[0] + 25, pixel_coord[1] + 170])
            item_to_inventory()
            total_items += 1

def move_to_stash(total_items):
    # divide the total_items, which is number of items in the moved to the 
    # inventory, by 5 which is the max slots per column. uses ceiling from math to 
    # round up which results in the total number of columns needed to click 
    # through.
    total_moved = 0
    for i in range(m.ceil(total_items / 5)):
        for j in range(5):
            if total_moved == total_items:
                return
            else:
                #print([INVENTORY_X_COORDS[i], INVENTORY_Y_COORDS[j]])
                gui.moveTo(INVENTORY_X_COORDS[i], INVENTORY_Y_COORDS[j])
                total_moved += 1
                item_to_inventory()

def search_and_move(search_name):
    total_items = 0
    for i in range(len(search_name)):
        if total_items >= 60:
            return(total_items)
        else:
            stash_search(search_name[i])
            t.sleep(1)
            total_items += move_from_stash()
            print(search_name)
    return(total_items)

#def scroll_and_put(tab_name, total_items, dump_position):
#    if total_items == 0:
#        return()
#    else:
#        number_of_scrolls = scroll_stash(tab_name)
#        move_to_stash(total_items)
#        print('moved', total_items)
#        total_items = 0
#        
#        # scroll back to where dump was found
#        for j in range(number_of_scrolls):
#            click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#        
#        # click on dump
#        #click_on_tab('dump')
#        t.sleep(0.5)
#        gui.moveTo(TAB_CLICK_COORDS[dump_position])
#        t.sleep(0.2)
#        gui.leftClick()

items = search_and_move(SORT_SEARCH_NAMES[10])

#gui.moveTo(RIGHT_ARROW_CLICK_COORDS)
#t.sleep(0.1)
#gui.leftClick()

gui.moveTo(RIGHT_ARROW_CLICK_COORDS)
t.sleep(0.1)
gui.leftClick()

gui.moveTo(RIGHT_ARROW_CLICK_COORDS)
t.sleep(0.1)
gui.leftClick()

gui.moveTo(TAB_CLICK_COORDS[6])
t.sleep(0.1)
gui.leftClick()

move_to_stash(items)

#gui.moveTo(LEFT_ARROW_CLICK_COORDS)
#t.sleep(0.1)
#gui.leftClick()

gui.moveTo(LEFT_ARROW_CLICK_COORDS)
t.sleep(0.1)
gui.leftClick()

gui.moveTo(LEFT_ARROW_CLICK_COORDS)
t.sleep(0.1)
gui.leftClick()

gui.moveTo(TAB_CLICK_COORDS[0])
t.sleep(0.1)
gui.leftClick()

# wont work for items larger than 1x1, need to develop a system for scanning
# inventory and putting those items different than 1 square at a time
for i in range(len(SORT_SEARCH_NAMES)):
    items = 0
    
    # single slot item
    if i <= 7:
        items = search_and_move(SORT_SEARCH_NAMES[i])
    
    # 4 slot item
    if 7 < i >= 9:
        items = search_and_move(SORT_SEARCH_NAMES[i])
        items = items * 4
        
    if i == 10:
        items = search_and_move(SORT_SEARCH_NAMES[i])
        items = items * 2
        
    if i > 10:
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
    elif items > 0 and i >= 6:
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
        
        gui.moveTo(TAB_CLICK_COORDS[0])
        t.sleep(0.1)
        gui.leftClick()

           
for i in range(len(SORT_SEARCH_NAMES)):
    if i <= 5:
         print('tab number ', i+1)
         
    if i >= 6:
        print('click right', i-6, ' times')
        print('tab number ', 6)
        print('click left', i-6, ' times')
            

##for i in range(len(STASH_TAB_NAMES)):
##    print(i, STASH_TAB_NAMES[i])
#
## find and click on a dump tab
#click_on_tab('dump')
#
## used to track the total items moved from the stash to the inventory
## later used to move the same number of items into the appropriate stash tab
##total_items = 0
#
#count = 0
#total_items = 0
#while count < 60:
#    for i in range(len(SORT_SEARCH_NAMES[i])):
#        items = 0
#        print(SORT_SEARCH_NAMES[i])
#        t.sleep(1)
#        items += 1
#    if items == 0:
#        count += 10
#        print(count)
#    elif items >= 1:
#        count += 1
#        print(count)
#print(total_items)
#
#fake_item_list = ['card', 'card', 'card']
#
#for i in range(len(SORT_SEARCH_NAMES[i])):
#    items = 0
#    if SORT_SEARCH_NAMES[i] == fake_item_list[0]:
#        items += 1
#        fake_item_list.pop
#if items == 0:
#    count += 10
#    print(count)
#elif items >= 1:
#    count += 1
#    print(count)
#
#
#
#
##!!!TODO!!!
##BREAK DOESNT WORK
## breaks out of the function if 60 items moved, which is max inventory
##def search_and_move(search_name):
##    count = 0
##    total_items = 0
##    while count < 60:
##        for i in range(len(search_name)):
##            stash_search(search_name[i])
##            t.sleep(1)
##            total_items += move_from_stash()
##        if total_items == 0:
##            count += 10
##            print(count)
##        elif total_items >= 1:
##            count += 1
##            print(count)
##        print(search_name)
##    return(total_items)
#    
#
#
##!!!TODO!!!
## NEED TO MAKE CHECKS FOR NON-SINGLE SPACE ITEMS (ARMOR, WEPS, ETC.)
## WHEN MOVING FROM INV TO STASH, IT CLICKS THE BOXES WHERE ITEMS MAY NOT EXIST
#
#total_items = 0
#items = 0
#for i in range(len(SORT_SEARCH_NAMES)):
#    items = search_and_move(SORT_SEARCH_NAMES[i])
#    scroll_and_put(STASH_TAB_NAMES[i], items, 0)
#
#
##for i in range(len(SORT_SEARCH_NAMES)):
##    if total_items >= 5:
##        scroll_and_put(STASH_TAB_NAMES[i], total_items, 0)
##    else: 
##        items = search_and_move(SORT_SEARCH_NAMES[i])
##        total_items += items
#    
#
#search_and_move(SORT_SEARCH_NAMES[0])
#scroll_and_put(STASH_TAB_NAMES[0], total_items, 0)
#
#total_items = 0
#for i in range(len(SORT_SEARCH_NAMES)):
#    items = 0
#    items = search_and_move(SORT_SEARCH_NAMES[i])
#    total_items += items
#    scroll_and_put(STASH_TAB_NAMES[i], total_items, 0)
#
#if total_items < 60: 
#    for i in range(len(SORT_SEARCH_NAMES)):
#        if i <= 3 and total_items <= 60:
#            stash_search(SORT_SEARCH_NAMES[i])
#            t.sleep(1)
#            total_items += move_from_stash()
#            print('item', i)
#
#        if (i == 3 or total_items == 60) and total_items != 0:
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print('moved', total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
#
#        if  3 < i <= 11 and total_items <= 60:
#            stash_search(SORT_SEARCH_NAMES[i])
#            t.sleep(1)
#            total_items += move_from_stash()
#            print('item', i)
#            
#        if (i == 11 or total_items == 60) and total_items != 0:
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print('moved', total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
#
#        if i == 12 or total_items == 60:
#            stash_search(SORT_SEARCH_NAMES[i])
#            t.sleep(1)
#            total_items += move_from_stash()
#            print('item', i)
#        
#        if (i == 12 or total_items == 60) and total_items != 0:
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print('moved', total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
#         
#        if i == 13 or total_items == 60:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#        
#        if (i == 13 or total_items == 60) and total_items != 0:
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print(total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
#
#        if i == 14 or total_items == 60:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#        
#        if (i == 14 or total_items == 60) and total_items != 0:
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print(total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
#
#        if (i == 15 or total_items == 60) and total_items != 0:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#            
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print(total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
#
#        if 15 < i <= 19 and total_items <= 60:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#
#        if (i == 19 or total_items == 60) and total_items != 0:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#            
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print(total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
#            
#        if (i == 20 or total_items == 60) and total_items != 0:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#            
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print(total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
#    
#        if (i == 21 or total_items == 60) and total_items != 0:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#            
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print(total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
#            
#        if (i == 22 or total_items == 60) and total_items != 0:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#            
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print(total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
#    
#        if 22 < i <= 24 and total_items <= 60:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#
#        if (i == 24 or total_items == 60) and total_items != 0:
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print(i)
#            print(total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#                
#        if (i == 25 or total_items == 60) and total_items != 0:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#            
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print(total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()     
#       
#        if (i == 26 or total_items == 60) and total_items != 0:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#            
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print(total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
#          
#        if 26 < i <= 32 and total_items <= 60:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#
#        if (i == 32 or total_items == 60) and total_items != 0:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#            
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print(total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
#            
#        if (i == 33 or total_items == 60) and total_items != 0:
#            stash_search(SORT_SEARCH_NAMES[i])
#            total_items += move_from_stash()
#            print(i)
#            
#            number_of_scrolls = scroll_stash(STASH_TAB_NAMES[i])
#            move_to_stash(total_items)
#            print(total_items)
#            total_items = 0
#            
#            # scroll back to where dump was found
#            for j in range(number_of_scrolls):
#                click_stash_arrow(LEFT_ARROW_CLICK_COORDS)
#            
#            # click on dump
#            click_on_tab('dump')
#            gui.leftClick()
            
#    # screenshot the stash
#    stash_shot = screenshot(ENTIRE_STASH_COORDS)
#    
#    # convert image to pixel map
#    stash_shot_pixels = stash_shot.load()
#    
#    # create empty list to store item yellow border coordinates
#    pixel_list = []
#    
#    for k in range(stash_shot.size[0]):
#        for l in range(stash_shot.size[1]):
#            if stash_shot_pixels[k,l] == YELLOW_BORDER:
#                pixel_list.append([k,l])
#                break
#
#    if len(pixel_list) == 0:
#        print('none found')
#        break
#    else:
#        gui.moveTo([pixel_list[0][0] + 25, pixel_list[0][1] + 170])
#        total_items += 1
#        item_to_inventory()










# Main sort function
# iterates through the SORT_SEARCH_NAMES list using the terms as items to
# search for, finds the highlighted item, moves it to the players inventory,
# finds and moves to the appropriate tab and moves the items from the inventory
# to the tab
            
# !!!TODO!!!
# NEED TO ADD BREAK THAT WHEN len(pixel_list) == 0: IT CHANGES FROM PULLING
# ITEMS OUT OF STASH TO MOVING TO THE NEW TAB AND PUTTING ITEMS
# COULD KEEP A COUNTER DEPENDING ON WHICH ITEMS ARE BEING PULLED REACHES
# MAX INVENTORY BEFORE SWITCHING MODES. Currency, essence, splinters, etc. 
# counts to 60, influenced counts to 6. 60 item slots in inventory.
# NEEDS TO CHECK FOR THE ITEM AGAIN AFTER MOVING TO INVENTORY AND BACK TO STASH
# UNLESS LIST WAS ALREADY AT 0 IN PREVIOUS CHECK
       
# NEEDS TO REVERSE THE NUMBER OF CLICKS IT MOVED TO FIND THE TAB TO DROP IN    
    
#for i in range(60):
#    #for j in range(len(SORT_SEARCH_NAMES)):
#    for j in range(1):
#        stash_search(SORT_SEARCH_NAMES[0])
#        stash_shot = screenshot(ENTIRE_STASH_COORDS)
#        
#        # convert image to pixel map
#        stash_shot_pixels = stash_shot.load()
#        
#        pixel_list = []
#        
#        for k in range(stash_shot.size[0]):
#                for l in range(stash_shot.size[1]):
#                    if stash_shot_pixels[k,l] == YELLOW_BORDER:
#                        pixel_list.append([k,l])
#                        break
#        if len(pixel_list) == 0:
#            break
#        else:
#            gui.moveTo([pixel_list[0][0] + 25, pixel_list[0][1] + 170])
#            move_to_inventory()
#
#
#len(parsed_text)
#       
#for i in range(8,11):
#    if re.search('esse', parsed_text[i]):
#        print(i)
#        gui.moveTo(TAB_CLICK_COORDS[1])
#    
#        print(parsed_text[8:11])
#        
#    
#    # split on \n
#    for i in range(len(parsed_text)):
#        parsed_text[i] = parsed_text[i].split('\n')
#     
#    # remove empty strings
#    for i in range(len(parsed_text)):
#        parsed_text[i] = [x for x in parsed_text[i] if x != '']
#        
#    # split on ~
#    for i in range(len(parsed_text[i])):
#        for j in range(len(parsed_text[j])):
#            parsed_text[i][j] = parsed_text[i][j].split(' ~ ')
#            
#    # unpack list of lists
#    for i in range(3):
#        parsed_text[i] = [x for l in parsed_text[i] for x in l]
#  
#    parsed_text[2][0]