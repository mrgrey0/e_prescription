from twilio.rest import Client

client = Client('AC21c1c76dcadf024fa600e9eaec2bb166', 'f14c815d0c085bc635cba13342751abe')


def sendMessage(num, text):
    message = client.messages \
        .create(
        body=text,
        from_='+18646063522',
        to=num
    )
