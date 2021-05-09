import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ledPin = 11
buttonPin = 12

GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)

while True:
    try:
        if GPIO.input(buttonPin):
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.5)
        else:
            GPIO.output(ledPin, GPIO.HIGH)
    except KeyboardInterrupt:
        GPIO.cleanup
        print("ended")
        exit()