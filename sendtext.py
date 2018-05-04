from twilio.rest import Client

"""Using Twilio, sends a Text Message to a Phone Number"""

account_sid = 'account_sid'
auth_token = 'auth_token'
my_cell = '+10digitmy#'
my_twilio = '+10digittwilio#'

message = 'Hello! Good Morning!'

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to=my_cell,
    from_=my_twilio,
    body= message)
