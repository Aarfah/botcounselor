import os, sys
from flask import Flask, request
from utils import wit_response
from pymessenger import Bot
import template

#initialise Flask app
app = Flask(__name__) 

PAGE_ACCESS_TOKEN = "EAAFGnmzStNcBAIVibLcyq18ZBXpgoNeeQSDhYq9qjcKiIGkvtEZB0ZCUVGyxuYg5bl6qeYiJB9apFXem2A1C7ZCyKrGHuxEKQsvD85bkXlkmHLCRIwRxyDhEZANMwTxoX6VU2co6Jm6LBpvA3p9a7WF614BgZBzHLOYukYZCzBKutF9TCEH94iv"

bot = Bot(PAGE_ACCESS_TOKEN)
i=0
m=[] 
@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
	# when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				# IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'

					# Echo
					#response = messaging_text
					m.append(i)
					response = None
					
					entity, value = wit_response(messaging_text)
					
					if entity == "daytype":
						response = "Why did you have a {} day?".format(str(value))
					elif entity == "name":
						response = "Hello! My name is Mitra.".format(str(value))
					elif entity == "sayhello":
						response = "Hello there, I'm Mitra! How was your day?"
					elif entity == "location":
						response = "So how is {}?".format(str(value))
					if response == None:
						response = "Sorry" 
					#m = messaging_text
					bot.send_text_message(sender_id,m[i]+response)
					#i = i + 1

	return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()

if __name__=="__main__":
   app.run(debug=True,port=80)