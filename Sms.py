 from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC52eada5c1aec227077f52a1dcb68e07d" 
AUTH_TOKEN = "f90acce48c7166facc9c0c989db0d403" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="+917899222034", 
	from_="+12028499994", 
	body="YOLO, Enjoy your life to the fullest :) asdfghjk",  
) 