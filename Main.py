import Sql
import measure
import threading
import webapi
import itertools
import requests
import time
import Sensor

height = 0

def measureHeight():
    while True:
        try:
            print("Initialising")
	    x=Sensor.Sensor(7,6)    #Second Pin must be PWM
	    for i in range(5):
		    print(x.measure())
	    h=x.measuremore(25)		  #returns distance in cm
	    print "Sane Measurement",h
	    return h
        except TypeError:
          continue
          # measureHeight()
if __name__=="__main__":
	
	
	t=measure.tank()
	t.select_max()
	s=Sql.Sql(t.height)
        height = t.height
	s.createTable()
	#volObj=litres.litres(t.height,t.diameter)
	#variable to keep track of the prev height and also  to help if the current goes off and reset
	prevPercentile  = 0 
	def do():
		global prevPercentile
		h = measureHeight()
		#volume=volObj.calculate(h)					 
		s.insertTable(h)
		print s.percentile
		
		try:
			webapi.sendData(s.percentile)
		except ValueError:
			print "Error"
			return
		
		print s.percentile
		prevPercentile = s.percentile
		#this block of code is for sending the info when the tank is getting filled up
		i=0
		while ( s.percentile > prevPercentile and s.percentile < 95):
			time.sleep(5)
			height = measureHeight()
			#volume=volObj.calculate(height)					 
			s.update_tb(height)
			if( ++i > 2 ):
				Thread = threading.Thread(webapi.sendData(s.percentile),args=())
				Thread.daemon=True
				thread.start
			prevPercentile = s.percentile
			
		if s.percentile < 10:
			print "low alert"
			#decrease the water flow rate of the valve
		
		if s.percentile> 95:
			print "High alert"
		
		if s.percentile == 100:
			print "full alert"

		
        for i in itertools.count():
                #Timer(1,do()).start()
                #Thread = threading.Thread(target=do(),args=())
                #Thread.start()
                do()
                time.sleep(20)
 
