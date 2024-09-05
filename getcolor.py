import cv2 as cv
import numpy as np
vid = cv.VideoCapture(0)

def get_caps_color(vid) -> str :
    """
    Return caps color 
    Blue : 1 
    Green : 2 
    White : 3
    Yellow : 4
    """
    mask_dict : list = [
        ((None,None,None),(None,None,None),"blue"),
        ((None,None,None),(None,None,None),"green"),
        ((None,None,None),(None,None,None),"white"),
        ((None,None,None),(None,None,None),"yellow"),
    ]
    while vid.isOpened():
        ret, frame = vid.read(0)
        print(np.shape(frame))
        cropped_image = frame[0:480,  80:560]
        hsv_image = cv.cvtColor(cropped_image,cv.COLOR_BGR2HSV) 
        cv.imshow("frame",hsv_image)
        if cv.waitKey(1) & 0xFF == ord('0'): 
            break
    color : str = None
    return color

get_caps_color(vid)