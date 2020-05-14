# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:38:23 2020

Program is written to read the screen while playing the game Path of Exile
Automatically crafts an item looking for specific mods and stops once the mods
have been achieved

@author: Eric

Game played on fullscreen borderless at 1920x1080
Coordinates to look within for text

top left inventory
(1000, 175, 1600, 640)

bottom right inventory
(1360, 500, 1920, 830)

bottom middle of stash tab
(20, 400, 580,745)

"""
from PIL import Image, ImageGrab
import os
import cv2
import pytesseract
import numpy as np

# set path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Manual test for a static image
# setup file location
#path = r'C:\Code projects\git projects\poe-autocrafter\images'
#file = 'stash1'
#full_path = os.path.join(path, file + '.png')

# uses pytess image to string pulling from the image with 
# language set to english
#text = pytesseract.image_to_string(full_path, lang = 'eng')

#print(text)

screen_cap = ImageGrab.grab(bbox = (20, 400, 580,745))

# used to open the image that is stored in screen_cap
#screen_cap.show()

tesstr = pytesseract.image_to_string( 
                cv2.cvtColor(np.array(screen_cap), cv2.COLOR_BGR2GRAY),  
                lang ='eng') 
print(tesstr) 

