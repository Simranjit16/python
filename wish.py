#!/usr/bin/python3
import datetime
d=datetime.datetime.now()
curhour=d.hour
curmint=d.minute
if curhour > 12:
	print("good morning")
else:
	if curhour > 12 and curhour < 16:
        	print("good after noon")
	else:
		if curhour > 16 and curhour < 20:
    			print("good evening")
		else:
			print("good night ")
