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
		response=requests.post(url,auth=('amar','dhruvadhruva'),data=values)
		return response.status_code
	except (requests.exceptions.Timeout,requests.exceptions.HTTPError,requests.exceptions.ConnectionError) as e:
			print "Error2",e
			raise ValueError
    
#def sendStatus():
#	values={
		
 #       "device": "dcbadcba",
  #      "on":"false",
  #      "order":"true"
  #      }
#	response=requests.put(url_status,auth=('amar','dhruvadhruva'),data=values)
#	print response.status_code
def sendOn(state):
	try:
		values={
		
		"device": "dcbadbca",
		"on":state,
		"order":state
		}
		print values
		response=requests.put(url_mystatus,auth=('dcbadcba','dcbadcba'),data=values)
		print response.status_code
	except (requests.exceptions.Timeout,requests.exceptions.HTTPError,requests.exceptions.ConnectionError) as e:
			print "Error2"
			raise ValueError 

if __name__=="__main__":
	sendData(30)
	print url_mystatus
	#sendStatus()
	#sendOn("false")
