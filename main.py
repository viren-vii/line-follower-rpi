import RPi.GPIO as GPIO
import time
import pins
import ir
import md


while True:
    IR = ir.IRread()
    #forward
    if(IR["IR1"] == 0 and IR["IR2"] == 0 and IR["IR3"] == 0 and IR["IR4"] == 1 and IR["IR5"] == 1 and IR["IR6"] == 0 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.forward(100, 100)

    if(IR["IR1"] == 0 and IR["IR2"] == 0 and IR["IR3"] == 0 and IR["IR4"] == 1 and IR["IR5"] == 0 and IR["IR6"] == 0 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.forward(100, 100)

    if(IR["IR1"] == 0 and IR["IR2"] == 0 and IR["IR3"] == 1 and IR["IR4"] == 0 and IR["IR5"] == 0 and IR["IR6"] == 0 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.forward(100, 100)

    #left
    if(IR["IR1"] == 1 and IR["IR2"] == 1 and IR["IR3"] == 1 and IR["IR4"] == 1 and IR["IR5"] == 0 and IR["IR6"] == 0 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.left(100, 100)

    if(IR["IR1"] == 0 and IR["IR2"] == 1 and IR["IR3"] == 1 and IR["IR4"] == 1 and IR["IR5"] == 0 and IR["IR6"] == 0 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.left(100, 100)

    if(IR["IR1"] == 0 and IR["IR2"] == 0 and IR["IR3"] == 1 and IR["IR4"] == 1 and IR["IR5"] == 0 and IR["IR6"] == 0 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.left(100, 100)

    if(IR["IR1"] == 1 and IR["IR2"] == 0 and IR["IR3"] == 1 and IR["IR4"] == 1 and IR["IR5"] == 0 and IR["IR6"] == 0 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.left(100, 100)

    if(IR["IR1"] == 1 and IR["IR2"] == 0 and IR["IR3"] == 0 and IR["IR4"] == 1 and IR["IR5"] == 0 and IR["IR6"] == 0 and IR["IR7"] == 0 and IR["IR8"] == 0):
        md.left(100, 100)
    

    #right
    if(IR["IR8"] == 1 and IR["IR7"] == 1 and IR["IR6"] == 1 and IR["IR5"] == 1 and IR["IR4"] == 0 and IR["IR3"] == 0 and IR["IR2"] == 0 and IR["IR1"] == 0):
        md.left(100, 100)

    if(IR["IR8"] == 0 and IR["IR7"] == 1 and IR["IR6"] == 1 and IR["IR5"] == 1 and IR["IR4"] == 0 and IR["IR3"] == 0 and IR["IR2"] == 0 and IR["IR1"] == 0):
        md.left(100, 100)

    if(IR["IR8"] == 0 and IR["IR7"] == 0 and IR["IR6"] == 1 and IR["IR5"] == 1 and IR["IR4"] == 0 and IR["IR3"] == 0 and IR["IR2"] == 0 and IR["IR1"] == 0):
        md.left(100, 100)

    if(IR["IR8"] == 1 and IR["IR7"] == 0 and IR["IR6"] == 1 and IR["IR5"] == 1 and IR["IR4"] == 0 and IR["IR3"] == 0 and IR["IR2"] == 0 and IR["IR1"] == 0):
        md.left(100, 100)

    if(IR["IR8"] == 1 and IR["IR7"] == 0 and IR["IR6"] == 0 and IR["IR5"] == 1 and IR["IR4"] == 0 and IR["IR3"] == 0 and IR["IR2"] == 0 and IR["IR1"] == 0):
        md.left(100, 100)
    
    #stop
    if(IR["IR8"] == 0 and IR["IR7"] == 0 and IR["IR6"] == 0 and IR["IR5"] == 0 and IR["IR4"] == 0 and IR["IR3"] == 0 and IR["IR2"] == 0 and IR["IR1"] == 0):
        md.stop(100, 100)

    #deg360
    if(IR["IR8"] == 1 and IR["IR7"] == 1 and IR["IR6"] == 1 and IR["IR5"] == 1 and IR["IR4"] == 1 and IR["IR3"] == 1 and IR["IR2"] == 1 and IR["IR1"] == 1):
        md.deg360(100, 100)
    
    