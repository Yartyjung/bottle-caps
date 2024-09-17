import serial
import time
# import cv2 as cv
# import getcolor
import RPi.GPIO as GPIO

SER = serial.Serial()

# Variable table

# vid = cv.VideoCapture("/dev/video0")
blue_button : int  = 26
green_button : int = 19
yellow_button : int = 13
relay : int = 20

def setup_serial(): 
    global SER 

    SER.port = "COM8"
    SER.baudrate = 9600
    SER.timeout = 1            #non-block read
    SER.xonxoff = False     #disable software flow control
    SER.rtscts = False     #disable hardware (RTS/CTS) flow control
    SER.dsrdtr = False       #disable hardware (DSR/DTR) flow control
    SER.bytesize = serial.EIGHTBITS #number of bits per bytes
    SER.parity = serial.PARITY_NONE #set parity check: no parity
    SER.stopbits = serial.STOPBITS_ONE #number of stop bits
    try: 
        SER.open()
    except Exception as e:
        print("error open serial port: " + str(e))
        exit()
    return SER

def response() -> str :
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

def convenyor(time : int) -> None : 
    """
    move convenyor equal to time input
    """
    GPIO.output(relay,True)
    time.sleep(time)
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

def main() -> None :
    # global vid
    pi_setup()
    while True :
        caps_color = None
        if GPIO.input(blue_button) == False :
            print("blue button")
        if GPIO.input(green_button) == False :
            print("green button")
        if GPIO.input(yellow_button) == False :
            print("yellow button")
        # serial_write("1")
        # caps_color : str = getcolor.get_caps_color(vid, False)
        if caps_color == "blue" :
            pass
        elif caps_color == "green" :
            pass
        elif caps_color == "white" :
            pass
        elif caps_color == "yellow":
            pass
        else:
            pass
    
if __name__ == "__main__" :
    main()