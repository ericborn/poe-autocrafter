# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:43:51 2020

@author: Eric

Functions relating to image manipulation
"""
from PIL import ImageGrab, ImageEnhance
from constants import WHITE_COLOR

# function takes an image as an input, creates a pixel map, iterates over the
# pixels and changes any blue ones to white. Helps tesseract read the text.
def color_text(img, value):
    # create a pixel map from the image
    img_pixels = img.load()
    # loops that evaluate the stash image pixels and change any blue to white
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            for k in range(len(value)):
                # change blue pixels to white
                if img_pixels[i,j] == value[k]:
                    img_pixels[i,j] = (WHITE_COLOR)
    return(img)

# Takes an image as input, resize the image to 3x original size 
# converts to b/w, create enhancer, apply contrast at 3 different values, 
# output list with b/w and 3 contrast adjusted images.
def image_adjustments(img): 
    # resizes image 3x larger 
    img = img.resize(((img.size[0] * 3),(img.size[1] * 3)))
    
    # convert enlarged image to black and white
    img = img.convert(mode='L')                
    
    # setup an enhancer for the black and white image
    img_enhancer = ImageEnhance.Contrast(img)
    
    # adjust contrast on the black and white imaqge
    img_enhance_1_5 = img_enhancer.enhance(1.5)
    img_enhance_2 = img_enhancer.enhance(2)
    img_enhance_2_5 = img_enhancer.enhance(2.5)
    
    # creates a list of the four images that were created
    stash_image_list = [img, img_enhance_1_5, img_enhance_2, \
                  img_enhance_2_5]
    return(stash_image_list)

# Testing functions
#stash_img = color_text(stash_img)
#img_list = image_adjustments(header_img)

# function that takes an input, coords, and makes a screenshot based upon them.
def screenshot(coords):
    img = ImageGrab.grab(bbox = (coords))
    return(img)
    