import cv2
import numpy as np

width = 200
height = 150
blank_img = np.zeros((height, width, 3))

cv2.imwrite('./image/blank.jpg', blank_img)
