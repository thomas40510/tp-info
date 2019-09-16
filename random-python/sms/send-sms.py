# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC7e92a00c50ac7d01f45bbf2d52f9f2c1'
auth_token = 'e54660379661df9522462625c35511ac'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+33755537325',
                     to='+33621041300'
                 )

print(message.sid)
