import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BOARD)
Left_wheel_GO =37
Left_wheel_BACK =35
Right_wheel_GO =38
Right_wheel_BACK =36
Direction = 0
bluetoothSerial = serial.Serial( "/dev/ttyAMA0", baudrate=9600 )
Input_Instruction = 0

GPIO.setup(Left_wheel_GO,GPIO.OUT)
GPIO.setup(Left_wheel_BACK,GPIO.OUT)
GPIO.setup(Right_wheel_GO,GPIO.OUT)
GPIO.setup(Right_wheel_BACK,GPIO.OUT)

def Forward():
    GPIO.output(Left_wheel_GO,GPIO.HIGH)
    GPIO.output(Left_wheel_BACK,GPIO.LOW)
    GPIO.output(Right_wheel_GO,GPIO.HIGH)
    GPIO.output(Right_wheel_BACK,GPIO.LOW)
    #time.sleep(0.5)

def Receding():
    GPIO.output(Left_wheel_GO,GPIO.LOW)
    GPIO.output(Left_wheel_BACK,GPIO.HIGH)
    GPIO.output(Right_wheel_GO,GPIO.LOW)
    GPIO.output(Right_wheel_BACK,GPIO.HIGH)
    #time.sleep(0.5)

def Turn_Left():
    GPIO.output(Left_wheel_GO,GPIO.LOW)
    GPIO.output(Left_wheel_BACK,GPIO.LOW)
    GPIO.output(Right_wheel_GO,GPIO.HIGH)
    GPIO.output(Right_wheel_BACK,GPIO.LOW)
    #time.sleep(1.5)

def Turn_Right():
    GPIO.output(Left_wheel_GO,GPIO.HIGH)
    GPIO.output(Left_wheel_BACK,GPIO.LOW)
    GPIO.output(Right_wheel_GO,GPIO.LOW)
    GPIO.output(Right_wheel_BACK,GPIO.LOW)
    #time.sleep(1.5)

def stop():
    GPIO.output(Left_wheel_GO,GPIO.LOW)
    GPIO.output(Left_wheel_BACK,GPIO.LOW)
    GPIO.output(Right_wheel_GO,GPIO.LOW)
    GPIO.output(Right_wheel_BACK,GPIO.LOW)

def readInput():
    Input_Instruction = bluetoothSerial.read()
    print Input_Instruction

print("Car is ready!")
try:
    while True:
        readInput()
        Direction = int(bluetoothSerial.read())
        if(Direction==1):
            Forward()
        elif (Direction==2):
            Receding()
        elif (Direction==3):
            Turn_Left()
        elif (Direction==4):
            Turn_Right()
        elif (Direction==0):
            stop()
        else :
            stop()
except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()
