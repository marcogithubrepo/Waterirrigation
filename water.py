import RPi.GPIO as GPIO
import time

#GPIO SETUP

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(channelsoilmoist, GPIO.IN)
#GPIO.setup(channeloutrele, GPIO.OUT)
#GPIO.output(channeloutrele,0)

class WaterPump(object):

        channelsoilmoist = 21
        channeloutrele = 4 
        countpump = 0
        countcheck = 0
        countpumptotal = 2
        countchecktotal = 5
        setcheck = True
        setpump = False

        def __init__(self):
		GPIO.setmode(GPIO.BCM)
                GPIO.setup(self.channelsoilmoist, GPIO.IN)
                GPIO.setup(self.channeloutrele, GPIO.OUT)
                GPIO.output(self.channeloutrele,GPIO.HIGH)

        #infinite loop
        #while True:
        #	time.sleep(1)
        
        def checkstartwater(self):        
                if self.setcheck == False:
                        self.countcheck += 1
                        print("time check: ", self.countcheck)
                        if self.setpump == True:
                                GPIO.output(self.channeloutrele,GPIO.HIGH )
                                self.countpump += 1
                                print("time pump: ", self.countpump)
                                if self.countpump >=  self.countpumptotal:
                                        self.countpump = 0
                                        self.setpump = False
                        else:
                                GPIO.output(self.channeloutrele,GPIO.LOW)
                                if self.countcheck >=  self.countchecktotal:
                                        self.countcheck = 0
                                        self.setcheck = True
                else:                                   	
                        if GPIO.input(self.channelsoilmoist):
                                self.setcheck = False
                                self.setpump = True
                                print("no water detected\n")
                                GPIO.output(self.channeloutrele,1 )
                                print("pumping water\n")
                        else:
                                self.setcheck = True
                                self.setpump = False
                                print("water detected")
                                GPIO.output(self.channeloutrele,0)
                
