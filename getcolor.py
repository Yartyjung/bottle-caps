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
    #score dictionary
    color_score = {"blue" : 0,
                   "green" : 0,
                   "white" : 0,
                   "yellow" : 0}
    
    #all the mask values store in a list
    mask_list : list = [
        ((85,115,0),(140,255,210),"blue")
        ((25,60,0),(95,255,255),"green"),
        ((50,0,116),(150,130,205),"white"),
        ((15,130,145),(147,195,210),"yellow")
    ]
    
    while True : 
        ret, frame = vid.read() 
        cv.imwrite("pic.png",frame)
        #resize the frame to 1:1 in the center
        cropped_image = frame[0:480,  80:560]
        
        #convert frame to HSV format
        hsv_image = cv.cvtColor(cropped_image,cv.COLOR_BGR2HSV)
        
        #for loop for masking 4 color
        for lower, upper, color in mask_list :
            
            #mask function
            mask = cv.inRange(hsv_image, np.array(lower), np.array(upper))
            
            #find all the masked area if there are any
            contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            
            #check if there are any contours if yes then calculate
            if contour is not None:
                areas = []
                for contour in contours :
                    
                    #find the contour area and append it for future calculations
                    area = cv.contourArea(contour)
                    areas.append(area)
            
            #calculate the score and edit the score dictionary
            color_score[color] = sum(areas) # type: ignore
            
            #if show_bool is true will do cv.imshow (for debug purpose only)
            if show_bool :
                filtered_frame = cv.bitwise_and(cropped_image, cropped_image, mask=mask)
                cv.imshow("frame",filtered_frame)
            
            if cv.waitKey(1) & 0xFF == ord('q'):
                exit()
        #get the max value and return it
        Key_max = max(color_score, key = color_score.get)   # type: ignore
        vid.release()
        return Key_max

get_caps_color(vid, False)