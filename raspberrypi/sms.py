import time
from sinchsms import SinchSMS

def sms(number,message):
    number = '+91'+number
    

    client = SinchSMS('1d3e1c97-bfa8-473a-8836-251eb8684b23','STIKhgUrlEGELD6dMD/bVQ==')

    print("Sending '%s' to %s" % (message, number))
    response = client.send_message(number, message)
    message_id = response['messageId']

    response = client.check_status(message_id)
    while response['status'] != 'Successful':
        print(response['status'])
        time.sleep(1)
        response = client.check_status(message_id)
        print(response['status'])

sms('9790180198','Alert - Tsunami Located 220km E of Kolata Impact time 20 mins Please move to higher attitute https://www.google.com/maps/place/Bay+of+Bengal/@15.0104041,81.4591314,5.55z/data=!4m5!3m4!1s0x30986dc9280955a1:0x1eb983108723598e!8m2!3d13.531665!4d87.5395855')