from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC301a60aeecca9df8918a56eb5dad3ece"
# Your Auth Token from twilio.com/console
auth_token  = "a9a9b49308f5cd4e6db84bea971d4e3d"
client = Client(account_sid, auth_token)
message = client.messages.create(
    to="+254719713296",
    from_="+14144099493",
    body="Our hearts have been touched by your readiness to save lives .We are inneed of more selfless people like you.Kindly visit http://127.0.0.1:8000/recipient/edit/5/ to update your information")
print(message.sid)