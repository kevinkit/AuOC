# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:30:47 2020

@author: Kevin
"""

import json
import glob
import cv2
import funcsToCall
import argparse

def parse_args():
    
    parser = argparse.ArgumentParser(description="A simple script for doing manual image augmentation, check the file funcsToCall to add custom functions")
    parser.add_argument("--source",default="saves",help="Path where the jsons are stored depicting the augmentations")
    parser.add_argument("--destination",default="results",help="Path where the augmented images are stored")
    args = parser.parse_args()
    return args

args = parse_args()


PATH_TO_LOAD_FROM = args.source
PATH_TO_SAVE_TO = args.destination


# get json files
json_files = glob.glob(PATH_TO_LOAD_FROM + "/" + "*.json")


for json_file in json_files:
    with open(json_file,"r") as f:
        data = json.load(f)
        
    orig_image = cv2.imread(data["filename"])
    for augmentation in data["augmentations"]:
        
        # TODO: only load functions once
        augFunc = getattr(funcsToCall,augmentation["func_name"])
        
        coords = augmentation["coordinates"]
                
        # copy out area and put it to the area
        cut = orig_image.copy()[coords[0]:coords[1],coords[2]:coords[3]]
    
        # do augmentation
        orig_image[coords[0]:coords[1],coords[2]:coords[3]] = augFunc(cut)
    
    ret = cv2.imwrite(PATH_TO_SAVE_TO + "/" + data["filename"].split("\\")[-1],orig_image)
    if not ret:
        print("could not save image!")