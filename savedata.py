import time
import datetime
import os
from os import path


class SaveData(object):
	def __init__(self):
		#remove file at startup if present
		try:
			if (path.isfile('data.txt')):
				os.remove("data.txt")
			else:
				print("nofile")
		except IOError:
			print( "Could not remove file!")

	def writedata(self, pumpingtime):
		try:
			f= open("data.txt","a")
			now = datetime.datetime.now()
#	                f.write(str(now.hour) + str(now.minute))
#        	        f.write(" ")
			f.write("%.4f\r\n"%pumpingtime)
			f.close()
		except IOError:
        		print( "Could not write file!")

 
