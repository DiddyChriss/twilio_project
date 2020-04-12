from twilio.rest import Client
from idproject import account_sid, auth_token, my_cell, my_twilio


client = Client(account_sid, auth_token)
my_msg = 'Test of messege with will sent To indicated Phone Number, like, "Hello DiddyChriss"'
message = client.messages.create(to = my_cell, from_ = my_twilio,
                                 body = my_msg)

