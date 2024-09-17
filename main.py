import serial
import time
import cv2 as cv
# import getcolor
import RPi.GPIO as GPIO
import numpy as np

SER = serial.Serial()

# Variable table

# vid = cv.VideoCapture("/dev/video0")
blue_button : int  = 26
green_button : int = 19
yellow_button : int = 13
relay : int = 20


def get_caps_color( show_bool : bool) -> str :
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
        ((85,95,80  ),(115,255,255),"blue")
        # ((None,None,None),(None,None,None),"green"),
        # ((None,None,None),(None,None,None),"white"),
        # ((None,None,None),(None,None,None),"yellow")
    ]
    
    vid = cv.VideoCapture(0)
    
    # while True : 
    ret, frame = vid.read() 
    
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
                cv.destroyAllWindows()
                vid.release()
    #get the max value and return it
    Key_max = max(color_score, key = color_score.get)   # type: ignore
    vid.release()
    return Key_max

def setup_serial(): 
    global SER 
    
    #start the serial port communication
    SER.port = "COM8"
    SER.baudrate = 9600
    SER.timeout = 1            #non-block read
    SER.xonxoff = False     #disable software flow control
    SER.rtscts = False     #disable hardware (RTS/CTS) flow control
    SER.dsrdtr = False       #disable hardware (DSR/DTR) flow control
    SER.bytesize = serial.EIGHTBITS #number of bits per bytes
    SER.parity = serial.PARITY_NONE #set parity check: no parity
    SER.stopbits = serial.STOPBITS_ONE #number of stop bits
    
    #to ensure that the serial port is on
    try: 
        SER.open()
    except Exception as e:
        print("error open serial port: " + str(e))
        exit()
    return SER

def response() -> bytes : #not used
    
    #read response from arduino
    response = SER.readline()
    print(response.decode("utf-8"))
    return response

def serial_write(text: str) -> None:
    setup_serial()
    if SER.isOpen():
        try:
            SER.flushIN() #flush IN buffer, discarding all its contents
            SER.flushOutput()#flush output buffer, aborting current output 
                             #and discard all that is in buffer
            byte_text = bytes(text,"utf-8")
            #write data
            SER.write(byte_text)
            print("write data: ",byte_text)

            SER.close()
        except Exception as e1:
            print ("error communicating...: " + str(e1))

def pi_setup() -> None :
    
    
    global blue_button
    global green_button
    global yellow_button
    global relay
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(blue_button,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    GPIO.setup(green_button,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    GPIO.setup(yellow_button,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    GPIO.setup(relay,GPIO.OUT)

def convenyor_stop() -> None :
    """
    stop the conveyor
    declare to be function for future implementation of feture
    """
    GPIO.output(relay,False)

def convenyor(sec : int) -> None : 
    """
    move convenyor equal to time input
    """
    GPIO.output(relay,True)
    time.sleep(sec)
    convenyor_stop()


def blue() -> None :
    serial_write("1")
    convenyor(1)

def green() -> None:
    serial_write("2")
    convenyor(1)

def white() -> None:
    serial_write("3")
    convenyor(1)

def yellow() -> None:
    serial_write("4")
    convenyor(1)

def dump() -> None:
    serial_write("0")
    convenyor(1)
    
def reset() -> None:
    serial_write("0")

def main() -> None :
    
    pi_setup()
    
    while True :
        time.sleep(0.1)
        caps_color = None
        if GPIO.input(blue_button) == False : # get cap color
            print("blue button")
            caps_color = get_caps_color(False) 
            if caps_color == "blue" :
                blue()
            elif caps_color == "green" :
                green()
            elif caps_color == "white" :
                white()
            elif caps_color == "yellow":
                yellow()
        if GPIO.input(green_button) == False : # reset main program
            print("green button")
            main()
        if GPIO.input(yellow_button) == False : # reset servo
            print("yellow button")
            reset()
            
    
if __name__ == "__main__" :
    main()