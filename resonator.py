# -*- coding: utf-8 -*-
"""
Created on Wed May 27 08:57:16 2020

@author: Eric
"""
import time as t
import math as m
import pyautogui as gui
from constants import FOSSIL_DICT, INVENTORY_X_COORDS,\
                      INVENTORY_Y_COORDS
                     #FOSSIL_NAMES, FOSSIL_COORDS, RESSONATORS,\ 
                     #RESONNATOR_COORDS, RESSONATOR_DICT

#!!!TODO!!!
# IF THE NUMBER OF RESONATORS LEFT IN THE STASH IS 1, WHEN IT SHIFT CLICKS NO
# DIALOG BOX APPEARS. POSSIBLY USE SCREEN READ BEFORE IT STARTS TO VERIFY 
# TOTAL AVAILABLE
# unstack and move
def unstack_and_move(item_type, number, x, y):
    gui.moveTo(FOSSIL_DICT[item_type])
    gui.keyDown('shift')
    gui.leftClick()
    gui.keyDown('enter')
    gui.keyUp('enter')
    gui.moveTo(INVENTORY_X_COORDS[x], INVENTORY_Y_COORDS[y])
    gui.leftClick()
    gui.keyUp('shift')

#!!!TODO!!!
# NEED 3 DIFFERENT PATHS DEPENDING ON RES SIZE 1,2,4
def resonator_unstack(res_type, foss_type, total_items): 
    total_moved = 0
    
    # single socket, 60 max
    if (res_type == 'primitive chaotic' or res_type == 'primitive alchemical')\
        and total_items <= 60:
        for i in range(m.ceil(total_items / 5)):
            for j in range(5):
                if total_moved == total_items:
                    return(total_moved)
                else:
                    #print([INVENTORY_X_COORDS[i], INVENTORY_Y_COORDS[j]])
                    unstack_and_move(res_type, total_items, i, j)
                    total_moved += 1
    if (res_type == 'primitive chaotic' or res_type == 'primitive alchemical')\
        and total_items > 60:
        return('Error, more resonators than space in inventory')
    return(total_moved)                
    # 2 socket, 24 max
    
    # 4 socket, 12 max

resonator_unstack('primitive alchemical', 5)

#def fossil_socket(foss_type, total_items, x, y):
#    gui.moveTo(FOSSIL_DICT[foss_type])
#    gui.keyDown('shift')
#    gui.leftClick()
#    gui.keyDown('enter')
#    gui.keyUp('enter')
#    gui.moveTo(INVENTORY_X_COORDS[x], INVENTORY_Y_COORDS[y])
#    gui.leftClick()
#    gui.keyUp('shift')

total_moved = 0
total_items = 5
for i in range(m.ceil(15 / 5)):
            for j in range(5):
                if total_moved == total_items:
                    print(total_moved)
                else:
                    #print([INVENTORY_X_COORDS[i], INVENTORY_Y_COORDS[j]])
                    unstack_and_move('primitive alchemical', total_items, i, j)
                    total_moved += 1