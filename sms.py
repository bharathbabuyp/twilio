from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "***" 
AUTH_TOKEN = "***" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
class twil:
	def __init__(self):
		self.name=self
	def sendsms(self,x):
		client.messages.create(
			to="+917899222034", 
			from_="+12028499994", 
			body=str(x),  
		) 
