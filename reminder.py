# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACb46dbcf191667d3b33907d168c7cbcec'
auth_token = 'removedforsecurity'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Kimberly, stop watching Tiktoks...',
                              from_='+12184223539',
                              to='+17147659279'
                          )

print(message.sid)

