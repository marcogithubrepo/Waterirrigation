import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(24, GPIO.OUT)
#GPIO.output(24,False)

class StartButton(object):

	startstate = False 
	
	def __init__(self):
		GPIO.output(24,False)

	def checkstartbutton(self):
		try: 

			button_state = GPIO.input(23)
			if button_state == False:
				print("Button pressed!")
				if self.startstate == False:
					GPIO.output(24, True)
					print("start!")
					self.startstate = True
				else:
					GPIO.output(24,False)
					print("stop!")
					self.startstate = False
			else:
				print("Button NOT pressed!")
			return 1;
		except:
			print("Exception..Cleaning GPIO")
			GPIO.cleanup()
			return 0;
