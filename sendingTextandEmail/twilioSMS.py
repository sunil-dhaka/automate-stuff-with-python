from email import message
from pydoc import cli
from cv2 import log
from twilio.rest import Client
import login
def twilioSMS(sms_body):
    sid=login.twilio_sid
    token=login.twilio_token

    client=Client(sid,token)

    message=client.messages.create(
        to=login.my_phone_no, # can not send sms to unverified numbers on twilio free account
        from_=login.twilio_phone_no,
        body=sms_body
    )

    print(message.sid)