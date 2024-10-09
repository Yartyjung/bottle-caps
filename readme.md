## Hello welcome to my duo mini project
In this project, my friend and I are developing a simple image processing system alongside some Arduino and Raspberry Pi components to create a bottle cap sorting machine.

> *this project we focused to improve our skill in coding,3d designing and hardware*


![the main image](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Frlv.zcache.com%2Fdnf_did_not_finish_funny_running_sticker-r218f23ec4f6c4776b69e1ff99a105e36_v9wz7_8byvr_512.jpg&f=1&nofb=1&ipt=e3efaa58ce75fddbd7a3457edfad659f5840f764732ee97472bdcc9918baa6a6&ipo=images)


### Main component
1. 200 cm x 200 cm 1.7 mm model paper
2. 4 MG90S servo motor 
3. 1 DC3V-6V DC Geared Motor
4. 1 L298 Dual H-Bridge Motor Driver
5. 1 LM2678 Step-Down Voltage Regulator
6. 1 Relay module
7. Rasberry pi 4 model B
8. Arduino R4 minima
9. Duct tape
10. Battery
11. Usb webcam
and some custom 3d printing parts ( you can find it [*Here*](https://github.com/Yartyjung/bottle-caps/tree/a059cf85aaac3480f4a38c41b6ffd8c11e5951a8/3d%20model) )

### Software
This project connects a Raspberry Pi and Arduino to control motors and servos, utilizing Raspberry Pi for motor control and image processing, while Arduino handles servo control. The devices communicate via serial using the [Pyserial library](https://pypi.org/project/pyserial/) for smooth operation.

The program flow is simple because the project involves only straightforward tasks. We organize all the code into functions, similar to block coding, so that in the main program, we simply call the functions in order.

it goes somthing like this 

```
def func1 ():
    ...
def func2 ():
    ...
def func3 ():
    ...
 
if __name__ == "__main__"
    fucn1()
    fucn2()
    fucn3()
```

### Hardware
We use [Onshape](https://www.onshape.com) for modeling before starting the actual build, as it saves us a lot of time during this phase and ensures the assembly process goes smoothly.