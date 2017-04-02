Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
import RPi.GPIO as GPIO
import time

# blinking function

def blink(pin):
    GPIO.output(40, GPIO.HIGH)
    print("LED is on")
    time.sleep(1)
    GPIO.output(40, GPIO.LOW)
    print("LED is off")
    time.sleep(1)
    return

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.OUT)

for i in range(0,50):
    blink(40)

GPIO.cleanup()

