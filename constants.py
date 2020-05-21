# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:27:29 2020

@author: Eric
"""

# various screen coordinate
# top of screen, stash/inventory
HEADER_COORDS = (0, 0, 1920, 90)

# top left inventory slot
TOP_LEFT_INVENTORY_COORDS = (1300, 610)

# item to be rolled in bottom middle of stash tab
ITEM_IN_STASH_COORDS = (355, 766)

# entire stash tab
ENTIRE_STASH_COORDS = (15, 170, 650, 750)

# currency description box when currency in top left of inventory
CURRENCY_DESCRIPTION_COORDS = (1060,410,1533,588)

# stash left arrow coordinates
LEFT_ARROW_COORDS = (14,130, 33,156)

# stash right arrow coordinates
RIGHT_ARROW_COORDS = (609,130, 626,156)

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
BLUE_COLOR = ((135, 135, 254), (98, 98, 188), (99, 99, 189), (74, 73, 142),\
               (74, 74, 142), (73, 73, 141), (127, 127, 239), (81, 81, 155),\
               (98, 98, 162), (108, 108, 178), (96, 96, 182), (125, 125, 233),\
               (108, 108, 181), (97, 97, 184), (123, 123, 233),(109, 109, 207))

# Grey stash arrow color
GREY_ARROW_COLOR = (31,31,31)

# Brown stash arrow color
BROWN_ARROW_COLOR = (55,23,1)

# String lists
# List of currency types
CURRENCY_NAMES = ['orb of alteration', 'chaos orb', 'orb of scouring', \
                  'orb of transmutation', 'regal orb']

# Text for the stash and inventory headers
HEADER_WORDS = ['stash','inventory']