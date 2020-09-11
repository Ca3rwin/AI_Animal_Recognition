# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:31:02 2020

@author: Caerwin
"""

import cv2            # For resizing images
import numpy as np
import os                          # For playing with directories
from random import shuffle
from tqdm import tqdm

TRAIN_DIR = 'train_and_test/train/train'
TEST_DIR = 'train_and_test/test/test'
IMG_SIZE = 50
LR = 1e-3                            # Learning rate