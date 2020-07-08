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
from roll_item import roll_item
import constants

# set path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = \
r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# create a list containing the words we're looking for in the image
header_words = ['stash','inventory']

currency_items = ['orb of alteration', 'chaos orb', 'orb of scouring', \
                  'orb of transmutation', 'regal orb']

#!!!TODO!!!
#THESE NEED TO COME IN FROM THE UI
# set desired mod and number of rolls to attempt
desired_mod = 'dexterity'
number_of_rolls = 5

# 1. check for stash/inventory being open
isc()


