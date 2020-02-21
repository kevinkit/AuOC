# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:53:37 2020

@author: Kevin
"""

import cv2
import math as m
def mosaic(img):
    """
        @brief function for pixelizing areas
        @param img Numpy array representing an image
        @return Will return the input img pixelized based on its size
    """
    width,height,channels = img.shape
    
    # the bigger the img the less pixels should be there
    pixels = int(m.sqrt(width*width + height*height))
    if pixels <= 0:
        pixels = 1
    pixel_size = int(1000*(1/pixels)) #int(m.sqrt(width*width + height*height))
    
    if pixel_size <= 0:
        pixel_size = 1
    re = cv2.resize(img,(pixel_size,pixel_size),interpolation=cv2.INTER_LINEAR)
    return cv2.resize(re, (height, width), interpolation=cv2.INTER_NEAREST)


def makeRed(img):
    img[:,:,-1] = 255
    return img

