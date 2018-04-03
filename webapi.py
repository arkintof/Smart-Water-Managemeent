#!/usr/bin/env python
import requests
from pytz import timezone
from datetime import datetime

#the url to which we post the data
url="https://smartwatermanagement.pythonanywhere.com/webapi/waterlevel/"
url_status="https://smartwatermanagement.pythonanywhere.com/webapi/devicestatus/dcbadcba/"
device  = ""
url_mystatus="https://smartwatermanagement.pythonanywhere.com/webapi/mystatus/dcbadcba/"
#setting location for the timezone
india=timezone('Asia/Kolkata')


def sendData(level):
	try:
		t=datetime.now(india)
		values={
		"time":t.isoformat(),
		"level":level,
		"device":"dcbadcba",
		"password":"dcbadcba"
		}
		#add your username and password in the below commented line
		#response=requests.post(url,auth=(username,password),data=values)  
		return response.status_code
	except (requests.exceptions.Timeout,requests.exceptions.HTTPError,requests.exceptions.ConnectionError) as e:
			print "Error2",e
			raise ValueError
 
def sendOn(state):
	try:
		values={
		
		"device": "dcbadbca",
		"on":state,
		"order":state
		}
		print values
		#add device username and password below
		#response=requests.put(url_mystatus,auth=(username,password),data=values)
		print response.status_code
	except (requests.exceptions.Timeout,requests.exceptions.HTTPError,requests.exceptions.ConnectionError) as e:
			print "Error2"
			raise ValueError 

if __name__=="__main__":
	sendData(30)
	print url_mystatus
	#sendStatus()
	#sendOn("false")
