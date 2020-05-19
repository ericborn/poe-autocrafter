# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:32:31 2020

@author: Eric

Used to find a particular tab within the inventory
"""
from image_manip import color_text, image_adjustments, screenshot

#!!!TODO!!!
# create function that takes tab name as input. Clicks tab scroll button to
# the left and screenshots. repeats until the tab names havent changed. If tab
# not found clicks right button x times and screenshots, parses text. Continues
# until tab is found

# stash left arrow coordinates
left_arrow_coords = (14,130, 33,156)

# stash right arrow coordinates
right_arrow_coords = (609,130, 626,156)

## grey arrow colors
#grey_arrow_colors = (31,31,31), (239,239,239), (32,32,32)
#
## brown arrow colors
#brown_arrow_colors = (55,23,1), (254,237,184), (81,38,0)

grey_arrow_value = (31,31,31)
brown_arrow_value = (55,23,1)


# screenshot left and right arrows
left_arrow_img = screenshot(left_arrow_coords)
right_arrow_img = screenshot(right_arrow_coords)

left_arrow_pixels = left_arrow_img.load()
right_arrow_pixels = right_arrow_img.load()

left = 0
right = 0
for i in range(left_arrow_img.size[0]):
    for j in range(left_arrow_img.size[1]):
        if left_arrow_pixels[i,j] == grey_arrow_value:
            left = 0
            right = 1


def check_arrow_grey(img):
    left = 0
    right = 0
    img_pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img_pixels[i,j] == grey_arrow_value:
                left = 0
                right = 1
            else:
                left = 1
                right = 0
    return(left, right)
    
check_arrow_grey(right_arrow_img)
