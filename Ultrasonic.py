#!/usr/bin/env python

print("Initialising")

import Sensor

if __name__ == "__main__":
    x=Sensor.Sensor(7,6)    #Second Pin must be PWM
    while(1):
        print(x.measure())  #returns distance in cm
    print "Sane Measurement",x.measuremore(25)
