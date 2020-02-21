# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:42:49 2020

@author: Kevin
"""
import cv2
import numpy as np
import argparse
import funcsToCall
import time
from ImageLoader import ImageLoader
import json

def parse_args():
    
    parser = argparse.ArgumentParser(description="A simple script for doing manual image augmentation, check the file funcsToCall to add custom functions")
    parser.add_argument("--save_path",default="saves",help="Path to save the augmentations to")
    parser.add_argument("--functions",default=["mosaic","makeRed"],nargs='+')
    parser.add_argument("--load_path",default="images/")
    args = parser.parse_args()
    return args


class MainClass():
    
    def __init__(self,
                 list_of_funcs=["mosaic",
                                "makeRed"],
                 save_mode=True):
        
        """
            @brief Class for handling the augmentation on images
            @param list_of_funcs Functions that are enabled and specified
            in the funcsToCall file
            @param save_mode Will determine wether to save the history of the 
            whole image augmenting
        """
    
        # this will save the augmentations if save mode is set to True
        self.history_object = []
        self.save_mode = save_mode
        self.mode_counter = 0
        self.mode = True
        self.drawing = False
        self.ix = -1
        self.iy = -1
        
        # initialising the image on a best guess
        self.img = np.zeros(shape=(512,512,3))
        
        self.list_of_func_names = list_of_funcs
        self.func_pointers = [getattr(funcsToCall,func_name) for \
                              func_name in list_of_funcs]

        self.func_counter = 0
        
    # mouse callback function
    def draw_circle(self,event,x,y,flags,param):
      #global ix,iy,drawing,mode

      if self.ix < x:
          start_x = self.ix
          end_x = x
      else:
          start_x = x
          end_x = self.ix
          
      if self.iy < y:
          start_y = self.iy
          end_y = y
      else:
          start_y = y
          end_y = self.iy


      if event == cv2.EVENT_LBUTTONDOWN:
          self.drawing = True
          self.ix,self.iy = x,y

      elif event == cv2.EVENT_MOUSEMOVE:
          #if mode == 0:
          if self.drawing == True:
              if self.mode == True:
                 
                  self.area = self.orig_image[start_y:end_y,start_x:end_x].copy()
                  f = self.func_pointers[self.func_counter]
                  print(f)
                  self.augmented = f(self.area)
                  self.img[start_y:end_y,start_x:end_x] = self.augmented

              else:
                  self.img[start_y:end_y,start_x:end_x] = self.orig_image[start_y:end_y,start_x:end_x]

      elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            if self.save_mode:
                history = {}
                if self.mode == True:
                    history["func_name"] = self.list_of_func_names[self.func_counter]
                else:
                    history["func_name"] = "undo"
                history["coordinates"] = [start_y,end_y,start_x,end_x]
                
                self.history_object.append(history)
            if self.mode == False:
                self.img[start_y:end_y,start_x:end_x] = self.orig_image[start_y:end_y,start_x:end_x]
 
    def setImage(self,img):
        """
            @brief Setter function for the image
            @param img Numpy array representing the Image
        """
        self.img = img
        self.orig_image = img.copy()
        return 0
    
    def nextFunc(self):
        if not self.func_counter == len(self.func_pointers) -1:
            self.func_counter += 1
            
    def lastFunc(self):
        if not self.func_counter == 0:    
            self.func_counter -= 1


args = parse_args() 
mc = MainClass(list_of_funcs=args.functions)
imL = ImageLoader(path_to_data=args.load_path)

img = imL.getCurrentImage()
mc.setImage(img)
cv2.namedWindow('image')

cv2.setMouseCallback('image',mc.draw_circle)


while(1):
 cv2.imshow('image',mc.img)
 k = cv2.waitKey(1) & 0xFF
 if k == ord('m'):
   mc.mode = not mc.mode
 elif k == ord("d"):
     complete_history = {}
     complete_history["augmentations"] = mc.history_object
     complete_history["filename"] = imL.current_file

     if mc.save_mode:
         with open(args.save_path + "/" + str(time.time()) + "_" + imL.current_file.split("\\")[-1] + ".json","w") as f:
             json.dump(complete_history,f)
         

     imL.next_file()

     mc.setImage(imL.getCurrentImage())
 elif k == ord("a"):
     imL.last_file()
     mc.setImage(imL.getCurrentImage())
 elif k == ord("k"):
     mc.nextFunc()
 elif k == ord("j"):
     mc.lastFunc()
 elif k == ord("s"):
    cv2.imwrite(args.save_path + "/" +str(time.time()) + "_" + imL.current_file.split("\\")[-1],mc.img)
 elif k == 27:
    break

cv2.destroyAllWindows() 