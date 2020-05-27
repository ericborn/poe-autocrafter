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


def move_from_stash(number, res_type):
    gui.moveTo(RESSONATOR_DICT[res_type])
    gui.keyDown('ctrl')
    for i in range(number):
        gui.leftClick()
    gui.keyUp('ctrl')


#!!!TODO!!!
# NEED 3 DIFFERENT PATHS DEPENDING ON RES SIZE 1,2,4
def resonator_unstack(number, res_type):  
    total_moved = 0
    
    # single socket, 60 max
    if res_type == 'primitive':
        for i in range(m.ceil(number / 5)):
            for j in range(5):
                if total_moved == number:
                    return
                else:
                    #print([INVENTORY_X_COORDS[i], INVENTORY_Y_COORDS[j]])
                    gui.moveTo(INVENTORY_X_COORDS[i], INVENTORY_Y_COORDS[j])
                    total_moved += 1
                    item_to_inventory()
                    
    # 2 socket, 24 max
    
    # 4 socket, 12 max