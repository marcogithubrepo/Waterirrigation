from startbutton import StartButton #button start water system class
from water import WaterPump #water pump and soil sensor class
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24,GPIO.OUT)
GPIO.output(24,False)

Stbtn = StartButton()
waterpump = WaterPump()

while True:
	time.sleep(1)
	Stbtn.checkstartbutton()
	print("startButton", Stbtn.startstate)
	if Stbtn.startstate:
                waterpump.checkstartwater()
	else:
		waterpump.stoppump()
	print("END")			

