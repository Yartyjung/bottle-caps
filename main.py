import serial
import time
import typing as t
import cv2 as cv
import getcolor
import 

SER = serial.Serial()
vid = cv.VideoCapture("coins_vid.mp4")
# blue green white yellow

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
            SER.flushInput() #flush input buffer, discarding all its contents
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
    pass

def convenyor() -> None :
    pass

def convenyot_stop() -> None :
    pass


def blue() -> None :
    serial_write("1")
    convenyor()

def green() -> None:
    serial_write("2")
    convenyor()

def white() -> None:
    serial_write("3")
    convenyor()

def yellow() -> None:
    serial_write("4")
    convenyor()

def dump() -> None:
    serial_write("0")
    convenyor()

def main() -> None :
    global vid

    serial_write("1")
    caps_color : str = getcolor.get_caps_color(vid, False)
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
        #dump
    
if __name__ == "__main__" :
    main()