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
#import re
#import pyautogui as gui
#import pytesseract
#from image_manip import color_text, image_adjustments, screenshot
from checks import check_for_mod as check_mod, check_inv_stash as check_inv, \
                   check_for_magic as check_magic, \
                   check_for_currency as check_currency
from roll_item import roll_item
from math import ceil, floor
#import constants

# set path to tesseract.exe
#pytesseract.pytesseract.tesseract_cmd = \
#r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#!!!TODO!!!
#THESE NEED TO COME IN FROM THE UI
# set desired mod and number of rolls to attempt
#desired_mod = 'flaring'

mod = 'polar' #'flaring'
currency_item = 'orb of alteration'
item_stack = 5 #20
number_of_rolls = 10
rolled_mods = []


perform_rolls(currency_item, mod, number_of_rolls)

# !!!TODO!!!
# implement stop if any of these fail
def perform_rolls(currency_item, desired_mod, roll_num):
    # max stack size for an alt is 20, divide the number of rolls by max stack
    # size and take the ceiling which will give the total number of stacks to
    # access
    total_rows = ceil(number_of_rolls / 20)
    
    # 5 rows per column
    #total_columns = ceil(total_rows / 5)
    
    # setup variables for while loop to process rolling
    row = 0
    col = 0
    roll = 0
    
    # 1. check for stash/inventory being open
    if check_inv() == -1:
        return('The stash and inventory are not both open. '\
              'Please open both and try again')
    else:
        print('The stash and inventory are both open.')

    # 2. check that the item is magic
    if check_magic() == -1:
        return('This item is not magic and cannot be alted.'\
              ' Place a magic item to be crafted.')
    else:
        print('This item is magic and can be alted.')
        
    # 3. check that mod doesnt already exist
    if check_mod(desired_mod) == -1:
        return('This item already has the desired mod.')
    else:
        print('No %s found' % desired_mod)
    
    # 4. check for currency
    if check_currency(currency_item) == 1:
        return('wrong type or missing currency.')
    else:
        print('Currency found')
    
#    # 5. Roll item
#    roll_item(0, 0)
#    
#    # 6. check for the mod
#    if check_mod(desired_mod) == -1:
#        return('This item already has the desired mod.')
#    else:
#        print('No %s found' % desired_mod)
    
    # gui.moveTo(INVENTORY_X_COORDS[0], INVENTORY_Y_COORDS[1])     
    # while loop than handles rolling
    # increments 0-4
    while roll < number_of_rolls:
        for item in range(item_stack):
            #print(item, col, row)
            
            # roll the item
            roll_item(col, row)
            # check for mod, break if the mod is found
            if check_mod(desired_mod) == -1:
                return('This item already has the desired mod.')
            else:
                print('No %s found' % desired_mod)
            roll += 1
                
        row += 1
        if row > 4:
            row = 0
            col += 1
