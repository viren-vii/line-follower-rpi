import RPi.GPIO as GPIO
import time
import pins

def forward(speed1, speed2):
    GPIO.output(pins.LM1, GPIO.HIGH)
    GPIO.output(pins.LM2, GPIO.LOW)
    GPIO.output(pins.RM1, GPIO.HIGH)
    GPIO.output(pins.RM2, GPIO.LOW)
    pins.EN1_PWM.ChangeDutyCycle(speed1)
    pins.EN2_PWM.ChangeDutyCycle(speed2)

def left(speed1, speed2):
    GPIO.output(pins.LM1, GPIO.LOW)
    GPIO.output(pins.LM2, GPIO.LOW)
    GPIO.output(pins.RM1, GPIO.HIGH)
    GPIO.output(pins.RM2, GPIO.LOW)
    pins.EN1_PWM.ChangeDutyCycle(speed1)
    pins.EN2_PWM.ChangeDutyCycle(0)

def right(speed1, speed2):
    GPIO.ouput(pins.LM1, GPIO.HIGH)
    GPIO.output(pins.LM2, GPIO.LOW)
    GPIO.output(pins.RM1, GPIO.LOW)
    GPIO.output(pins.RM2, GPIO.LOW)
    pins.EN1_PWM.ChangeDutyCycle(0)
    pins.EN2_PWM.ChangeDutyCycle(speed2)

def reverse(speed1, speed2):
    GPIO.output(pins.LM1, GPIO.LOW)
    GPIO.ouput(pins.LM2, GPIO.HIGH)
    GPIO.output(pins.RM1, GPIO.LOW)
    GPIO.output(pins.RM2, GPIO.HIGH)
    pins.EN1_PWM.ChangeDutyCycle(speed1)
    pins.EN2_PWM.ChangeDutyCycle(speed2)

def stop(speed1, speed2):
    GPIO.output(pins.LM1, GPIO.LOW)
    GPIO.output(pins.LM2, GPIO.LOW)
    GPIO.output(pins.RM1, GPIO.LOW)
    GPIO.output(pins.RM2, GPIO.LOW)

def deg360(speed1, speed2):
    GPIO.output(pins.LM1, GPIO.HIGH)
    GPIO.output(pins.LM2, GPIO.LOW)
    GPIO.output(pins.RM1, GPIO.LOW)
    GPIO.ouput(pins.RM2, GPIO.HIGH)
    pins.EN1_PWM.ChangeDutyCycle(speed1)
    pins.EN2_PWM.ChangeDutyCycle(speed2)