from startbutton import StartButton #button start water system class
from water import WaterPump #water pump and soil sensor class
import time
import datetime
import RPi.GPIO as GPIO
import os
from os import path


GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24,GPIO.OUT)
GPIO.output(24,False)

Stbtn = StartButton()
waterpump = WaterPump()
count = 0

try:
	if (path.isfile('data.txt')):
		os.remove("data.txt")
	else:
		print("nofile")
                      
		
except IOError:
    	print( "Could not remove file!")


while True:
	time.sleep(0.5)
	Stbtn.checkstartbutton()
	print("startButton", Stbtn.startstate)
#	waterpump.checkstartwater()
	if Stbtn.startstate:
        	waterpump.checkstartwater()
		test = 0
	else:
		waterpump.stoppump()
        

	#write plot data
	if( (count  %  600  == 0) or (count == 0)):
		try:
			f= open("data.txt","a")
			now = datetime.datetime.now()
        		print("Write!", count)
#	                f.write(str(now.hour) + str(now.minute))
#        	        f.write(" ")
                	f.write("%d\r\n"%waterpump.pumpingtime)
			f.close()
		except IOError:
        		print( "Could not write file!")
	count += 1


