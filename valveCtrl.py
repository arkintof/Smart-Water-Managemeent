import webapi
import mraa
import FetchJson
import time
 
URL = "https://smartwatermanagement.pythonanywhere.com/webapi/mystatus/dcbadcba/"
 
class ValveCtrl:
	scanTime = None
	
	def __init__(self,switchPin):
		print("ValvePin is",switchPin)
		self.switch = mraa.Gpio(switchPin)
		self.switch.dir(mraa.DIR_OUT)
	
	def Switch(self,state):
                print state
		self.switch.write(state)
		self.state = True
	
	def Close(self):
		self.switch.write(0)
		self.state = False

	
if __name__ == "__main__":
        state =1 
        valve = ValveCtrl(8)
        valve.Switch(state)
        while(1):
	    js = FetchJson.get_json_from_url(URL)
	    state = FetchJson.get_text(js)
            print "stateis:",state
            valve.Switch(state is False)
	    webapi.sendOn(state)
	    #time.sleep(1)
		
	
	
