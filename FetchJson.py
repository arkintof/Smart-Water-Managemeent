
import requests
import json
URL = "https://smartwatermanagement.pythonanywhere.com/webapi/mystatus/dcbadcba/"


def get_url(url):
    response = requests.get(url,auth=('dcbadcba', 'dcbadcba'))
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    js = get_json_from_url(url)
    return js

def get_text(updates):
	num_updates = updates["order"]
	return num_updates 

if __name__=="__main__":
    js=get_json_from_url(URL)
    print js
    print get_text(js) is False
 
