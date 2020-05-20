# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:38:23 2020

Program is written to read the screen while playing the game Path of Exile
Automatically crafts an item looking for specific mods and stops once the mods
have been achieved

@author: Eric

Game played on windowed fullscreen at 1920x1080
Coordinates for an empty stash tab to look within for text
(15, 170 , 650, 750)

testing at windowed 800x600, game in top left corner produced worse results

Scaling image by 3x produces much better results than the native resolution

Enhancing contrast by 2 also improves parsing results, 1.5 and 2.5 produce
worse results

!!!TODO!!!
CREATE UI/WEBPAGE

IMPLEMENT FASTER CHECK FOR MOD

OUTPUT CURRENT ROLL/TOTAL ROLLS COUNTER
??OUTPUT ROLLS PASSED TO LOG FILE??

details on converting python to standalone exe
https://stackoverflow.com/questions/5458048/how-to-make-a-python-script-standalone-executable-to-run-without-any-dependency
"""
import re
import pyautogui as gui
import pytesseract
from image_manip import color_text, image_adjustments, screenshot
from checks import check_for_mod as cfm, inv_stash_check as isc

# set path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = \
r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# static values
# various screen coordinate
# top of screen, stash/inventory
header_coords = (0, 0, 1920, 90)

# top left inventory slot
top_left_inventory_coords = (1300, 610)

# item to be rolled in bottom middle of stash tab
item_in_stash_coords = (355, 766)

# entire stash tab
stash_coords = (15, 170, 650, 750)

# currency description box when currency in top left of inventory
currency_description_coords = (1060,410,1533,588)

# grey RGB value for a normal item
grey_value = (200, 200, 200)

# yellow RGB value for a rare item
yellow_value = (254, 254, 118)

# greyish yellow RGB values for a currency item
currency_value = ((170,158,129), (140,129,105), (150,139,113), (156,145,117))

# blue RGB values for magic a item
blue_value = ((135, 135, 254), (98, 98, 188), (99, 99, 189), (74, 73, 142),\
               (74, 74, 142), (73, 73, 141), (127, 127, 239), (81, 81, 155),\
               (98, 98, 162), (108, 108, 178), (96, 96, 182), (125, 125, 233),\
               (108, 108, 181), (97, 97, 184), (123, 123, 233),(109, 109, 207))

# create a list containing the words we're looking for in the image
currency_items = ['orb of alteration', 'chaos orb', 'orb of scouring', \
                  'orb of transmutation', 'regal orb']

#!!!TODO!!!
#THESE NEED TO COME IN FROM THE UI
# set desired mod and number of rolls to attempt
desired_mod = 'dexterity'
number_of_rolls = 5

# <= 0 mod not found, >=1 mod found
cfm(desired_mod)

# -1 indicates stash or inventory is not open, 1 indicates both are open
isc()


def roll_me(mod, rolls):
    # move mouse to item location in stash tab 355, 766
    gui.moveTo(item_in_stash_coords)
    gui.PAUSE = 0.1
    
    # screenshot the stash tab with the item to be crafted
    stash_img = screenshot(stash_coords)
    
    # create a pixel map from the image
    stash_img_pixels = stash_img.load()
    
    # checks the color of the item to ensure its a magic item
    for i in range(stash_img.size[0]):
        for j in range(stash_img.size[1]):
            if stash_img_pixels[i,j] == yellow_value:
                raise Exception('This item is rare and cannot be alted. ' \
                        'Place a magic item to be crafted.')
            if stash_img_pixels[i,j] == grey_value:
                raise Exception('This item is normal and cannot be alted. ' \
                        'Place a magic item to be crafted.')
    
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






# 3. screenshot currency item description and parse
# move cursor to first item slot in inventory 1300, 615
gui.moveTo(top_left_inventory_coords)

# take a screenshot of the currency item description
currency_img = screenshot(currency_description_coords)

# colors the currency image item name to white
color_text(currency_img, currency_value)

# perform adjustments
currency_img = image_adjustments(currency_img)

#inventory_img = screenshot(top_left_inventory_coords)
#inventory_img = image_adjustments(inventory_img)

# parse the image for text
currency_text = []

for i in range(len(currency_img)):
    currency_text.append(pytesseract.image_to_string(currency_img[i], \
                                                          lang='eng', config =\
                                                          '--psm 12').lower())

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
    raise Exception('You do not have currency in your inventory.' \
                    'Place it in the top left inventory slot dummy.') 

# executes the mod check and rolls until the desired mod is found or max 
# attempts are met
roll_me(desired_mod, number_of_rolls)