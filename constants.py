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

# entire stash tab
ENTIRE_STASH_COORDS = (12, 162, 647, 792)

# coords for the boarders of each stash tab
TAB_BOARDER_COORDS = ((43,130,120,156), (130,130,208,156),(220,130,291,156),  
                      (302,130,362,156),(374,130,434,156),(447,130,516,156),
                      (529,130,594,156))

# Coordinates for cursor positions
# top left of screen, cannot use 0,0, triggers an autogui fail-safe
TOP_LEFT_CORNER = (50, 50)

# top left inventory slot
TOP_LEFT_INVENTORY_COORDS = (1300, 610)

# item to be rolled in bottom middle of stash tab
ITEM_IN_STASH_COORDS = (355, 766)


# coords for clicking stash tab arrows
LEFT_ARROW_CLICK_COORDS = (25,145)
RIGHT_ARROW_CLICK_COORDS = (615,145)

# click locations for each stash tab
TAB_CLICK_COORDS = ((80,145), (165,145), (255,145), (330,145), (400,145), 
                    (480,145), (560,145))

INVENTORY_Y_COORDS = [612,667,720,773,822]

INVENTORY_X_COORDS = [1296,1350,1403,1457,1507,1562,
                      1614,1666,1718,1770,1822,1874]


# stash search box
STASH_SEARCH_BOX = (520, 895)

# Colors
# White used to color text
WHITE_COLOR = (255, 255, 255)

# grey RGB value for a normal item
GREY_ITEM_COLOR = (200, 200, 200)

# grey RGB values for item mod text
GREY_COLOR = ((128,128,128), (75,75,75),(93,93,93),(112,112,112), (81,81,81),
              (120,120,120), (108,108,108), (116,116,116), (103,103,103),
              (124,124,124), (98,98,98), (67,67,67))

# yellow RGB value for a rare item
YELLOW_ITEM_COLOR = (254, 254, 118)

# greyish yellow RGB values for a currency item
CURRENCY_ITEM_COLOR = ((170,158,129),(140,129,105),(150,139,113),(156,145,117))

# blue RGB values for magic a item
BLUE_COLOR = ((135,135,254), (98,98,188), (99,99,189), (74,73,142),
              (74,74,142), (73,73,141), (127,127,239), (81,81,155),
              (98,98,162), (108,108,178), (96,96,182), (125,125,233),
              (108,108,181), (97,97,184), (123,123,233), (109,109,207))
               
# Grey stash arrow color
GREY_ARROW_COLOR = (31,31,31)

# Brown stash arrow color
BROWN_ARROW_COLOR = (55,23,1)

# primary color of black text on stash tabs
BLACK_TEXT = (42,28,13)

# primary color of yellow text on stash tabs
YELLOW_TEXT = (216,162,98)

# Border around the highlighted item in stash
YELLOW_BORDER = (231,180,119)

# stash brown text
STASH_YELLOW_TEXT = ((216,162,98), (162,125,70),  (162,126,70),  (159,119,108),
                    (210,158,95),  (210,157,95),  (191,144,85),  (198,150,89),
                    (203,152,100), (171,119,70),  (113,84,130),  (254,192,118),
                    (163,112,83),  (142,87,80),   (143,95,50),   (162,116,66),
                    (100,74,108),  (197,147,89),  (191,142,85),  (155,114,67),
                    (127,93,54),   (110,80,46),   (178,134,82),  (247,187,114),
                    (211,158,96),  (240,182,111))

STASH_BLACK_TEXT = ((42,28,13), (60,53,47), (53,38,13), (85,57,10), (81,55,11),
                    (84,82,80), (32,59,8),  (53,48,45), (89,58,7),  (28,67,7),
                    (15,91,3),  (93,60,7),  (38,25,11), (45,35,26), (59,52,47),
                    (57,50,47), (33,30,28), (29,23,17), (27,17,6),  (29,22,17),
                    (85,83,81), (63,58,52), (66,60,56), (73,69,67), (35,22,9), 
                    (75,73,71), (51,46,43))

# String lists
# List of currency types
CURRENCY_NAMES = ['orb of alteration', 'chaos orb', 'orb of scouring',
                  'orb of transmutation', 'regal orb']

# Text for the stash and inventory headers
HEADER_WORDS = ['stash','inventory']

EQUIPMENT_SORTING_INDEX = [4, 8, 1, 1, 1, 1, 4, 1, 1, 1, 2, 1, 1, 6, 1]

# Names for the stash tabs, used for sorting
STASH_TAB_NAMES = ['dump', 'incu', 'misc', 'splt', 'esse', 'prop', 'veil', 
                   'card', 'jewl', 'foss', 'curr', 'gems', 'maps', 'unqe',
                   'infl']                       

# dict with only 1x1 items
STASH_DICT = {'dump': 0,
              'oils': 1,
              'tane': 2,
              'deli': 3,
              'incu': 4,
              'card': 5,
              'frag': 6,
              'esse': 7,
              'prop': 8,
              'jewl': 9,
              'foss': 10,
              '$$$$': 11,
              'gems': 12,
              'maps': 13}

# full list with larger than 1x1 items
#STASH_DICT = {'dump': 0, 
#              'misc': 1, 
#              'incu': 2, 
#              'splt': 3, 
#              'esse': 4, 
#              'prop': 5, 
#              'veil': 6, 
#              'card': 7, 
#              'jewl': 8, 
#              'foss': 9, 
#              'curr': 10, 
#              'gems': 11, 
#              'maps': 12, 
#              'unqe': 13,
#              'infl': 14}

# list with only 1x1 items
SORT_SEARCH_NAMES = [['oil'], ['tane\'s', 'abrasive catalyst', 
                     'tempering catalyst', 'fertile catalyst', 
                     'prismatic catalyst', 'intrinsic catalyst', 
                     'imbued catalyst', 'turbulent catalyst'], ['simulacrum', 
                     'delirium orb'], ['incubator'],['card'], 
                    ['splinter of','scarab', 'sacrifice at dawn', 'timeless',
                     'sacrifice at dusk', 'fragment of', 'divine vessel',
                     'sacrifice at noon', 'sacrifice at midnight', 'mortal',  
                     'offering to the goddess'],['essence'],
                     ['prophecy to your'],['eye jewel',
                     'cobalt jewel','viridian jewel','crimson jewel'],
                     ['"place in a resonator"', 'primitive resonator',
                     '"requires 4"', '"requires 3"', '"requires 2"'],
                     ['currency', 'stacked deck'],['quality gem', 'vaal gem'],
                     ['Map']]
                     


# full list with larger than 1x1 items
#SORT_SEARCH_NAMES = [['oil','tane\'s','stacked deck', 'delirium orb'],
#                     ['incubator'], ['splinter of','scarab',
#                     'sacrifice at dawn', 'sacrifice at dusk', 
#                     'sacrifice at noon', 'sacrifice at midnight', 'timeless', 
#                     'divine vessel', 'offering to the goddess'],['essence'],
#                     ['prophecy to your'],['veiled'],['card'],
#                     ['eye jewel','cobalt jewel','viridian jewel', 
#                     'crimson jewel'],['fossil'],['currency', 
#                     'simulacrum'],['quality gem','vaal gem'],['Map'],
#                     ['unique'],['shaper','elder', 'redeemer', 'crusader', 
#                     'warlord', 'hunter']]

# dictionary with mods and their stats                   
MOD_DICT = {'polar' : r'adds.+(cold damage)',
            'flaring' : r'adds.+(physical damage)'}

# Fossil tab
FOSSIL_DICT = {'jagged': (129,236),
               'dense': (197,236),
               'frigid': (266,236),
               'aberrant': (333,236),
               'scorched': (398,236),
               'metallic': (467,236),
               'pristine': (534,236),
               'bound': (66,300),
               'corroded': (129,300),
               'perfect': (197,300),
               'prismatic': (266,300),
               'enchanted': (333,300),
               'aetheric': (398,300),
               'lucent': (467,300),
               'serrated': (534,300),
               'shuddering': (600,300),
               'tangled': (101,371),
               'bloodstained': (168,371),
               'gilded': (266,371),
               'encrusted': (329,371),
               'sanctified': (398,371),
               'hollow': (501,371),
               'fractured': (564,371),
               'glyphic': (129,435),
               'faceted': (534,435),
               'primitive alchemical': (130,606),
               'primitive chaotic': (527,606),
               'potent alchemical': (84,688),
               'powerful alchemical': (174,688),
               'prime alchemical': (275,688),
               'prime chaotic': (381,688),
               'powerful chaotic': (483,688),
               'potent chaotic': (573,688)}
    
#FOSSIL_NAMES = ['jagged', 'dense', 'frigid', 'aberrant', 'scorched', 
#                'metallic', 'pristine', 'bound', 'corroded', 'perfect', 
#                'prismatic', 'enchanted', 'aetheric', 'lucent', 'serrated',
#                'shuddering', 'tangled', 'bloodstained','gilded', 'encrusted', 
#                'sanctified', 'hollow', 'fractured', 'glyphic', 'faceted']

#FOSSIL_COORDS = [(129,236), (197,236), (266,236), (333,236), (398,236),
#                    (467,236), (534,236), (66,300),  (129,300), (197,300),
#                    (266,300), (333,300), (398,300), (467,300), (534,300),
#                    (600,300), (101,371), (168,371), (266,371), (329,371),
#                    (398,371), (501,371), (564,371), (129,435), (534,435)]

#RESSONATORS = ['primitive alchemical', 'primitive chaotic', 
#               'potent alchemical', 'powerful alchemical', 'prime alchemical',
#               'prime chaotic', 'powerful chaotic','potent chaotic']
#
#RESONNATOR_COORDS = [(130,606), (527,606), (84,688), (174,688), (275,688),
#                        (381,688), (483,688), (573,688)]