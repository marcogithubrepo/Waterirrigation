import RPi.GPIO as GPIO
import time
import datetime

#GPIO SETUP

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(channelsoilmoist, GPIO.IN)
#GPIO.setup(channeloutrele, GPIO.OUT)
#GPIO.output(channeloutrele,0)

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
#	f= open("data.txt","w+")



        def __init__(self):
		GPIO.setmode(GPIO.BCM)
                GPIO.setup(self.channelsoilmoist, GPIO.IN)
                GPIO.setup(self.channeloutrele, GPIO.OUT)
                GPIO.output(self.channeloutrele,GPIO.HIGH) #swichoff pump at startup
#		now = datetime.datetime.now()
#                self.f.write(str(now.hour) + str(now.minute))
#                self.f.write(" ")
#                self.f.write("%d\r\n"%self.pumpingtime)
#		print("WRITE!")


	def __del__(self):
 		f.close()
	    
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
		self.pumpingtime += 1
		#write data on file
#		now = datetime.datetime.now()
#                self.f.write(str(now.hour) + str(now.minute))
#                self.f.write(" ")
#                self.f.write("%d\r\n"%self.pumpingtime)
