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
        countpumptotal = 2 #pumping time
        countchecktotal = 180 #check waitinig time after pump
        setcheck = True  #bolean to check soil sensor (after pumping delay before checking thee sensor again
        setpump = False #bolean to start the pump

        def __init__(self):
		GPIO.setmode(GPIO.BCM)
                GPIO.setup(self.channelsoilmoist, GPIO.IN)
                GPIO.setup(self.channeloutrele, GPIO.OUT)
                GPIO.output(self.channeloutrele,GPIO.HIGH) #swichoff pump at startup

        
        def checkstartwater(self):        
                if self.setcheck == False:
                        self.countcheck += 1
                        print("time check: ", self.countcheck)
                        if self.setpump == True:
                                #GPIO.output(self.channeloutrele,GPIO.LOW)
                                self.startpump()
				self.countpump += 1
                                print("time pump: ", self.countpump)
                                if self.countpump >=  self.countpumptotal:
                                        self.countpump = 0
                                        self.setpump = False
                        else:
                                #GPIO.output(self.channeloutrele,GPIO.HIGH)
                                self.stoppump()
				if self.countcheck >=  self.countchecktotal:
                                        self.countcheck = 0
                                        self.setcheck = True
                else: #check soil sensor enable                                  	
                        if GPIO.input(self.channelsoilmoist):
                                self.setcheck = False
                                self.setpump = True
                                print("no water detected\n")
#                                GPIO.output(self.channeloutrele,GPIO.LOW )
                                print("pumping water\n")
				self.startpump()
                        else:
                                self.setcheck = True
                                #self.setpump = False
                                print("water detected")
				self.stoppump()
#                                GPIO.output(self.channeloutrele,GPIO.HIGH)
                
	def stoppump(self):
		self.setpump = False
		GPIO.output(self.channeloutrele, GPIO.HIGH)

	def startpump(self):
		GPIO.output(self.channeloutrele, GPIO.LOW)
