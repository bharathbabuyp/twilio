# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Get these credentials from http://twilio.com/user/account
account_sid = "AC52eada5c1aec227077f52a1dcb68e07dd"
auth_token = "f90acce48c7166facc9c0c989db0d4033"
client = TwilioRestClient(account_sid, auth_token)

# Make the call
call = client.calls.create(to="+917899222034",  # Any phone number
                           from_="+12028499994 ", # Must be a valid Twilio number
                           url="https://handler.twilio.com/twiml/EHf5217307363a4acc57551cd75a9fad6f")
print(call.sid)
