import RPi.GPIO as GPIO
import time
import pins
def IRread():
    return {"IR1": GPIO.input(pins.IR1), "IR2": GPIO.input(pins.IR2), "IR3": GPIO.input(pins.IR3), "IR4": GPIO.input(pins.IR4), "IR5": GPIO.input(pins.IR5), "IR6": GPIO.input(pins.IR6), "IR7": GPIO.input(pins.IR7), "IR8": GPIO.input(pins.IR8)}
# while True:
# IR1 = GPIO.input(pins.IR1)
    # IR2 = GPIO.input(pins.IR2)
    # IR3 = GPIO.input(pins.IR3)
    # IR4 = GPIO.input(pins.IR4)
    # IR5 = GPIO.input(pins.IR5)
    # IR6 = GPIO.input(pins.IR6)
    # IR7 = GPIO.input(pins.IR7)
    # IR8 = GPIO.input(pins.IR8)