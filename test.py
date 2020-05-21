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
from checks import check_for_mod as cfm, check_inv_stash as isc
from roll_item import roll_item

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










# executes the mod check and rolls until the desired mod is found or max 
# attempts are met
roll_item(desired_mod, number_of_rolls)
