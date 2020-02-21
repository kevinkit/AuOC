# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:56:21 2020

@author: Kevin
"""
import glob
import cv2
class ImageLoader():
    
    def __init__(self,
                 path_to_data="images/",
                 fileending="*"):
        
        self.path_to_data = path_to_data
        self.cnt = 0
        self.files = glob.glob(path_to_data + "*." + fileending)
        self.current_file = self.files[0]
        
    def next_file(self):
        """
            @brief Will load the next filename in the buffer, if the maximum
            is reached, it will stay at the end
        """        
        if not self.cnt == len(self.files) -1:
            self.cnt +=1
        self.current_file = self.files[self.cnt]
    
    def last_file(self):
        """
            @brief Will load the last filename in the buffer, if the first name
            is reached it will stay there
        """
        if not self.cnt == 0:    
            self.cnt -= 1
        self.current_file = self.files[self.cnt]
        
    def getCurrentImage(self):
        img  = cv2.imread(self.current_file)
        if img is None:
            raise FileNotFoundError("could not find file",self.current_file)
        return img





        
        
        