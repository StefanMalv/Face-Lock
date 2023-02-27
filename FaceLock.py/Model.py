import splitfolders as sf
import pandas as pd
import cv2 as cv
import numpy as np
import os
from Objects import user1

class_name = user1.first

#data splitt into test, train and validation dataset
def split(class_name):

    outputfolders = f"data_for_model_{class_name}"

    sf.ratio("C:\\Users\\stefa\\OneDrive\\Skrivebord\\Kode ting\\DATA", output=outputfolders, 
            seed=42, ratio=(.7, .2, .1),
            group_prefix=None)


split(class_name)