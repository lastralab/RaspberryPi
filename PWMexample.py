import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 50)
pwm.start(0)
print("Let's fade!")
try:
    while True:
        for i in range(100):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(100, 0, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.02)
except KeyboardInterrupt:
    GPIO.cleanup() #Ctrl+C to exit
    print("Good bye!")

