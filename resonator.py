# -*- coding: utf-8 -*-
"""
Created on Wed May 27 08:57:16 2020

@author: Eric
"""
import time as t
import pyautogui as gui
from constants import FOSSIL_DICT, RESSONATOR_DICT
                     #FOSSIL_NAMES, FOSSIL_COORDS, RESSONATORS,\ 
                     #RESONNATOR_COORDS
                      

for i in FOSSIL_DICT:
    gui.moveTo(FOSSIL_DICT[i])
    t.sleep(1)

FOSSIL_DICT[0]


def resonator_unstack(number, res_type):
    gui.moveTo(RESONNATOR_COORDS[res_type])
    