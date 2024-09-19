import serial
import time
import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)
while True:
    ret,frame = vid.read()
    hsvFrame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    yellow_max = np.array([85,115,0],dtype="uint8")
    yellow_min = np.array([140,255,210],dtype="uint8")
    yellow_mask = cv.inRange(hsvFrame,yellow_min,yellow_max)


    cv.imshow("original",frame)
    cv.imshow("masked",yellow_mask)