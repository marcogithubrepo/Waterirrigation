import RPi.GPIO as GPIO
import time

#GPIO SETUP
channelsoilmoist = 21
channeloutrele = 20 
GPIO.setmode(GPIO.BCM)
GPIO.setup(channelsoilmoist, GPIO.IN)
GPIO.setup(channeloutrele, GPIO.OUT)
GPIO.output(channeloutrele,0)

countpump = 0
countcheck = 0
countpumptotal = 5
countchecktotal = 180
setcheck = True
setpump = False

#infinite loop
while True:
	time.sleep(1)
	
	if setcheck == False:
                countcheck += 1
                print("time check: ", countcheck)
                if setpump == True:
                        GPIO.output(channeloutrele,1 )
                        countpump += 1
                        print("time pump: ", countpump)
                        if countpump >=  countpumptotal:
                                countpump = 0
                                setpump = False
                else:
                        GPIO.output(channeloutrele,0)
                        if countcheck >=  countchecktotal:
                                countcheck = 0
                                setcheck = True
        else:                                   	
		if GPIO.input(channelsoilmoist):
			setcheck = False
			setpump = True
			print("no water detected\n")
			GPIO.output(channeloutrele,1 )
			print("pumping water\n")
		else:
                        setcheck = True
			setpump = False
			print("water detected")
			GPIO.output(channeloutrele,0)
	
