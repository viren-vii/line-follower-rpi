import RPi.GPIO as GPIO
import time
import pins
import ir
import md

while True:
    IR = ir.IRread()
    IR["IR4"]=IR["IR5"]
    print(IR)
    #forward
    if(IR["IR1"] == 0 and IR["IR2"] == 0 and IR["IR3"] == 0 and IR["IR4"] == 1 and IR["IR5"] == 1 and IR["IR6"] == 0 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.forward(50, 50)

    if(IR["IR1"] == 0 and IR["IR2"] == 0 and IR["IR3"] == 1 and IR["IR4"] == 1 and IR["IR5"] == 1 and IR["IR6"] == 1 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.forward(50, 50)

    if(IR["IR1"] == 0 and IR["IR2"] == 0 and IR["IR3"] == 1 and IR["IR4"] == 1 and IR["IR5"] == 1 and IR["IR6"] == 0 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.forward(50, 50)

    if(IR["IR1"] == 0 and IR["IR2"] == 0 and IR["IR3"] == 0 and IR["IR4"] == 1 and IR["IR5"] == 1 and IR["IR6"] == 1 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.forward(50, 50)

    if(IR["IR1"] == 0 and IR["IR2"] == 0 and IR["IR3"] == 1 and IR["IR4"] == 0 and IR["IR5"] == 0 and IR["IR6"] == 1 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.forward(50, 50)

    if(IR["IR1"] == 0 and IR["IR2"] == 0 and IR["IR3"] == 0 and IR["IR4"] == 0 and IR["IR5"] == 0 and IR["IR6"] == 0 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.stop(50, 50)
    