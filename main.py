# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:38:23 2020

Program is written to read the screen while playing the game Path of Exile
Automatically crafts an item looking for specific mods and stops once the mods
have been achieved

@author: Eric

Game played on fullscreen borderless at 1920x1080
Coordinates to look within for text
top left
1000x175

top right
1600x175

bottom left
1000x640

bottom right
1600x640
"""
from PIL import ImageGrab
import os
import cv2
import pytesseract

# setup file location
path = r'C:\Code projects\git projects\poe-autocrafter\images'
file = 'stash1'
full_path = os.path.join(path, file + '.png')

# set path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# uses pytess image to string pulling from the image with 
# language set to english
text = pytesseract.image_to_string(full_path, lang = 'eng')

print(text)


