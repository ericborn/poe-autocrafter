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
from math import ceil
#import constants

# set path to tesseract.exe
#pytesseract.pytesseract.tesseract_cmd = \
#r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#!!!TODO!!!
#THESE NEED TO COME IN FROM THE UI
# set desired mod and number of rolls to attempt
#desired_mod = 'flaring'

mod = 'burning'
currency_item = 'orb of alteration'
item_stack = 20
number_of_rolls = 10

perform_rolls(mod, number_of_rolls)

# !!!TODO!!!
# implement stop if any of these fail
def perform_rolls(desired_mod, roll_num):
    # max stack size for an alt is 20, divide the number of rolls by max stack
    # size and take the ceiling which will give the total number of stacks to
    # access
    stacks = ceil(number_of_rolls / 20)
    columns = ceil(stacks / 5)
    
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
    check_mod(desired_mod)
    
    # 4. check for currency
    check_currency()
    
    # trying to create a loop that will actually perform the number of stacks
    # instead of defaulting to total columns all rows
    
    #col = 0
    #row = 5    
      
    #for stack in range(stacks):
    #    print(stack, stack % 5)
    #    
    #row % 5
    #    
    #for column in range(columns):
    #    row += 1
    #    if row % 5 == 0 
    #        for stack in range(stack % 5):
    #        #for row in range(5):
    #            print(column, stack % 5)
    # gui.moveTo(INVENTORY_X_COORDS[0], INVENTORY_Y_COORDS[1]) 
            
    for col in range(columns):
        for row in range(5):
            #print(col,row)
            for item in range(item_stack):
                print(item, col, row)
                #roll_item(col, row)
                if check_mod(desired_mod) == 1:
                    return(desired_mod, 'rolled')
    
    # Roll item
    roll_item()
    
    # check for mod again
    check_mod(desired_mod)