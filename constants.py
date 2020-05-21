# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:27:29 2020

@author: Eric
"""

# Coordinates for screenshots
# top of screen, stash/inventory
HEADER_COORDS = (0, 0, 1920, 90)

# currency description box when currency in top left of inventory
CURRENCY_DESCRIPTION_COORDS = (1060,410,1533,588)

# stash left arrow coordinates
LEFT_ARROW_COORDS = (14,130, 33,156)

# stash right arrow coordinates
RIGHT_ARROW_COORDS = (609,130, 626,156)

# all tabs in the stash
STASH_TAB_COORDS = (35, 128, 606, 158)

# Coordinates for cursor positions
# top left of screen
TOP_LEFT_CORNER = (0, 0)

# top left inventory slot
TOP_LEFT_INVENTORY_COORDS = (1300, 610)

# item to be rolled in bottom middle of stash tab
ITEM_IN_STASH_COORDS = (355, 766)

# entire stash tab
ENTIRE_STASH_COORDS = (15, 170, 650, 750)

# Colors
# White used to color text
WHITE_COLOR = (255, 255, 255)

# grey RGB value for a normal item
GREY_ITEM_COLOR = (200, 200, 200)

# yellow RGB value for a rare item
YELLOW_ITEM_COLOR = (254, 254, 118)

# greyish yellow RGB values for a currency item
CURRENCY_ITEM_COLOR = ((170,158,129), (140,129,105), (150,139,113), (156,145,117))

# blue RGB values for magic a item
BLUE_COLOR = ((135,135,254), (98,98,188), (99,99,189), (74,73,142),
              (74,74,142), (73,73,141), (127,127,239), (81,81,155),
              (98,98,162), (108,108,178), (96,96,182), (125,125,233),
              (108,108,181), (97,97,184), (123,123,233), (109,109,207))
               
# Grey stash arrow color
GREY_ARROW_COLOR = (31,31,31)

# Brown stash arrow color
BROWN_ARROW_COLOR = (55,23,1)

# stash brown text
STASH_BROWN_TEXT = ((216,162,98), (162,125,70), (162,126,70),
                    (210,158,95), (191,144,85), (198,150,89),
                    (203,152,100), (171,119,70), (113,84,130),(159,119,108),
                    (163,112,83), (142,87,80), (143,95,50), (162,116,66),
                    (100,74,108),(197,147,89), (191,142,85), (155,114,67),
                    (127,93,54),(110,80,46), (178, 134, 82))

STASH_BLACK_TEXT = ((42,28,13), (60,53,47), (53,38,13), (85,57,10),
                    (81,55,11), (84,82,80), (32,59,8), (53,48,45),
                    (89,58,7), (28,67,7), (15,91,3), (93,60,7))

# String lists
# List of currency types
CURRENCY_NAMES = ['orb of alteration', 'chaos orb', 'orb of scouring', \
                  'orb of transmutation', 'regal orb']

# Text for the stash and inventory headers
HEADER_WORDS = ['stash','inventory']