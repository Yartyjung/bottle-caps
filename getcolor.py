import cv2 as cv
import numpy as np
vid = cv.VideoCapture(0)

def get_caps_color(vid , show_bool : bool) -> str :
    """
    Return caps color 
    Blue : 1 
    Green : 2 
    White : 3
    Yellow : 4
    """
    blue : list = []
    color_score = {"blue" : None,
                   "green" : None,
                   "white" : None,
                   "yellow" : None}
    mask_dict : list = [
        ((85,95,80  ),(115,255,255),"blue")
        # ((None,None,None),(None,None,None),"green"),
        # ((None,None,None),(None,None,None),"white"),
        # ((None,None,None),(None,None,None),"yellow")
    ]
    while True : 
        ret, frame = vid.read() 
        cropped_image = frame[0:480,  80:560]
        hsv_image = cv.cvtColor(cropped_image,cv.COLOR_BGR2HSV)
        for lower, upper, color in mask_dict :
            mask = cv.inRange(hsv_image, np.array(lower), np.array(upper))
            contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            areas = 0
            for contour in contours :
                area = cv.contourArea(contour)
                areas.append(area)
            color_score[color] = sum(areas)
            if show_bool :
            # filtered_frame = cv.bitwise_and(cropped_image, cropped_image, mask=mask)
            # cv.imshow("frame",filtered_frame)
                pass
            if cv.waitKey(1) & 0xFF == ord('q'):
                exit()
        # color : str = None
        # return color

get_caps_color(vid)