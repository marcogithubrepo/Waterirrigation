import RPi.GPIO as GPIO 
import time 
import datetime
# Import the ADS1x15 module.
import Adafruit_ADS1x15

class WaterPump(object):
	waterpercentage = 0.00
	waterthr = 7000
	pumpingtime = 0
	GAIN = 1
	adc = Adafruit_ADS1x15.ADS1115()
#	channelsoilmoist=21 #water sensor digital input
	channeloutrele = 4 #turn on water pump rele
	channeloutsensoron = 17 #turn on soil sensor channle
	countpump = 0
	countcheck = 0
	countpumptotal = 1  #pumping time x 0.5 sec
	countchecktotal = 360  #check waitinig time after pump x 0.5 sec
	setcheck = True  #bolean to check soil sensor (after pumping delay before checking thee sensor again
	setpump = False #bolean to start the pump


	def __init__(self):
		GPIO.setmode(GPIO.BCM)
#		GPIO.setup(self.channelsoilmoist, GPIO.IN)
		GPIO.setup(self.channeloutsensoron, GPIO.OUT)
		GPIO.output(self.channeloutsensoron,GPIO.LOW)
		GPIO.setup(self.channeloutrele, GPIO.OUT)
		GPIO.output(self.channeloutrele,GPIO.HIGH) #swichoff pump at startup

	def __del__(self):
		GPIO.cleanup()

	def checkstartwater(self):
		self.checkpercentage()
		print(self.waterpercentage)
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
			if self.waterpercentage < self.waterthr:
				self.setcheck = False
				self.setpump = True
				print("no water detected\n")
				print("pumping water")
				self.startpump()
			else:
				self.setcheck = True
				print("water deteccted")
				self.stoppump()
			
	def stoppump(self):
		self.setpump = False
		GPIO.output(self.channeloutrele, GPIO.HIGH)
		print("stoppump")

	def startpump(self):
		GPIO.output(self.channeloutrele, GPIO.LOW)
		print("startpump")
		self.pumpingtime += 1

	def checkpercentage(self):
		try:
			GPIO.output(self.channeloutsensoron, GPIO.HIGH)
			self.waterpercentage =(32767 - self.adc.read_adc(0, gain=self.GAIN))/32767*10000
			GPIO.output(self.channeloutsensoron, GPIO.LOW)
		except:
    			print("error reading gpio")



