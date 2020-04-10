import RPi.GPIO as GPIO
import time
import datetime

class WaterPump(object):

	pumpingtime = 0
        channelsoilmoist = 21
        channeloutrele = 4 
        countpump = 0
        countcheck = 0
        countpumptotal = 1  #pumping time x 0.5 sec
        countchecktotal =360  #check waitinig time after pump x 0.5 sec
        setcheck = True  #bolean to check soil sensor (after pumping delay before checking thee sensor again
        setpump = False #bolean to start the pump


        def __init__(self):
		GPIO.setmode(GPIO.BCM)
                GPIO.setup(self.channelsoilmoist, GPIO.IN)
                GPIO.setup(self.channeloutrele, GPIO.OUT)
                GPIO.output(self.channeloutrele,GPIO.HIGH) #swichoff pump at startup


	def __del__(self):
                GPIO.cleanup()
	    
        def checkstartwater(self):
              
                if self.setcheck == False:
                        self.countcheck += 1
                        print("time check: ", self.countcheck)
                        if self.setpump == True:
                                self.startpump()
				self.countpump += 1
                                print("time pump: ", self.countpump)
                                if self.countpump >=  self.countpumptotal:
                                        self.countpump = 0
                                        self.setpump = False
                        else:
                                self.stoppump()
				if self.countcheck >=  self.countchecktotal:
                                        self.countcheck = 0
                                        self.setcheck = True
                else: #check soil sensor enable                                  	
                        if GPIO.input(self.channelsoilmoist):
                                self.setcheck = False
                                self.setpump = True
                                print("no water detected\n")
                                print("pumping water\n")
				self.startpump()
                        else:
                                self.setcheck = True
                                print("water detected")
				self.stoppump()
                
	def stoppump(self):
		self.setpump = False
		GPIO.output(self.channeloutrele, GPIO.HIGH)

	def startpump(self):
		GPIO.output(self.channeloutrele, GPIO.LOW)
		self.pumpingtime += 1

