
import os

from telesign.messaging import MessagingClient


# Replace the defaults below with your Telesign authentication credentials or pull them from environment variables.
customer_id = '80A36A19-25FF-4D9C-B9D9-D4240CD84DE7'
api_key = 'GHGsyVXUduEppKiM6iGv3jA0gn495+WgiB33NzNiUdFXpxSvR7TiD+sH33ClxCuQXWyRBMHB3hAipaRNDWvCug=='

# Set the default below to your test phone number or pull it from an environment variable. 
# In your production code, update the phone number dynamically for each transaction.
phone_number = '917350314101'

# Set the message text and type.
message = "SMS service is working"
message_type = "ARN"

# Instantiate a messaging client object.
messaging = MessagingClient(customer_id, api_key)

# Make the request and capture the response.
#response = messaging.message(phone_number, message, message_type)
def sendMessage(num,text):
    response = messaging.message(num, text, message_type)
    return response.body

# Display the response body in the console for debugging purposes. 
# In your production code, you would likely remove this.
if __name__ == '__main__':
    print(sendMessage('917350314101','its working'))