import pika
from time import sleep
import requests
import simplejson as json

## Configuration
#url = 'SUMO_URL_HERE'
#apiuser = 'API_USER'
#queuename = 'QUEUE_NAME'
#apipass = 'PASSWORD'
#headers = {'Content-type': 'application/json'}

#connection = pika.BlockingConnection() # pass in the BlockingConnection that includes a connection url
print("before connection")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="export-streaming.amp.cisco.com", port=443,credentials=pika.PlainCredentials(username=apiuser, password=apipass), ssl=True))
print("after connection")
channel = connection.channel()
print("after channel")

method_frame, header_frame, body = channel.basic_get(queuename)
print("after channel.basic_get")
if method_frame:
 print(body)
 r = requests.post(url, data=body, headers=headers)
 channel.basic_ack(method_frame.delivery_tag)
else:
 print('No message returned')
