#Pushbutton + LED
# Author: Niam Moltta
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.OUT)

try:
    while True:
        inputValue= GPIO.input(12)
        if (inputValue == False): #Not pressed
            print("LED is blinking")
            GPIO.output(16, True) 
            time.sleep(1)
            GPIO.output(16, False)
            time.sleep(1)
        else: #Pressed
            GPIO.output(16, True) #LED ON
            time.sleep(0.03)
            print("LED is on")
except KeyboardInterrupt:
    print("Cleaning up GPIO...")
    GPIO.cleanup()
