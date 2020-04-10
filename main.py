from startbutton import StartButton #button start water system class
from water import WaterPump #water pump and soil sensor class
from savedata import SaveData #Write data to file class
import time
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

Stbtn = StartButton()
waterpump = WaterPump()
Savedt = SaveData()
count = 0


while True:
	time.sleep(0.5)
	Stbtn.checkstartbutton()
	print("startButton", Stbtn.startstate)

	#check startbuttonstatus
	if Stbtn.startstate:
        	waterpump.checkstartwater()
	else:
		waterpump.stoppump()
	#write plot data
	if( (count  %  600  == 0) or (count == 0)):
		print(count)
                Savedt.writedata(waterpump.pumpingtime)
	
	count+=1                




