# -*- coding: utf-8 -*-
"""
Created on Wed May 27 08:57:16 2020

@author: Eric
"""
import time as t
import math as m
import pyautogui as gui
from constants import FOSSIL_DICT, RESSONATOR_DICT, INVENTORY_X_COORDS,\
                      INVENTORY_Y_COORDS
                     #FOSSIL_NAMES, FOSSIL_COORDS, RESSONATORS,\ 
                     #RESONNATOR_COORDS
                      

for i in FOSSIL_DICT:
    gui.moveTo(FOSSIL_DICT[i])
    t.sleep(1)

for i in RESSONATOR_DICT:
    gui.moveTo(RESSONATOR_DICT[i])
    t.sleep(1)
    
    
gui.moveTo(RESSONATOR_DICT['primitive alchemical'])
gui.keyDown('shift')
gui.leftClick()
gui.keyDown('enter')
gui.keyUp('enter')
gui.moveTo(INVENTORY_X_COORDS[0], INVENTORY_Y_COORDS[0])
gui.leftClick()
gui.keyUp('shift')


# unstack and move
def unstack_and_move(res_type, number, x, y):
    gui.moveTo(RESSONATOR_DICT[res_type])
    gui.keyDown('shift')
    gui.leftClick()
    gui.keyDown('enter')
    gui.keyUp('enter')
    gui.moveTo(INVENTORY_X_COORDS[x], INVENTORY_Y_COORDS[y])
    gui.leftClick()
    gui.keyUp('shift')

#!!!TODO!!!
# NEED 3 DIFFERENT PATHS DEPENDING ON RES SIZE 1,2,4
def resonator_unstack(res_type, total_items): 
    total_moved = 0
    
    # single socket, 60 max
    if (res_type == 'primitive chaotic' or res_type == 'primitive alchemical')\
        and total_items <= 60:
        for i in range(m.ceil(total_items / 5)):
            for j in range(5):
                if total_moved == total_items:
                    return
                else:
                    #print([INVENTORY_X_COORDS[i], INVENTORY_Y_COORDS[j]])
                    unstack_and_move(res_type, total_items, i, j)
                    total_moved += 1
    if (res_type == 'primitive chaotic' or res_type == 'primitive alchemical')\
        and total_items <= 60:
        return('Error')
    return(total_moved)                
    # 2 socket, 24 max
    
    # 4 socket, 12 max
    
resonator_unstack('primitive alchemical', 8)
