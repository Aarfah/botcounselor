import os, sys
from flask import Flask, request
from utils import wit_response
from pymessenger import Bot
import mysql.connector
import curl
#initialise Flask app
app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAFGnmzStNcBAIVibLcyq18ZBXpgoNeeQSDhYq9qjcKiIGkvtEZB0ZCUVGyxuYg5bl6qeYiJB9apFXem2A1C7ZCyKrGHuxEKQsvD85bkXlkmHLCRIwRxyDhEZANMwTxoX6VU2co6Jm6LBpvA3p9a7WF614BgZBzHLOYukYZCzBKutF9TCEH94iv"

bot = Bot(PAGE_ACCESS_TOKEN)
i=0


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
					#m.append(messaging_text)
					response = None
					cnx = mysql.connector.connect(user='sql12229537',password='fduArMVZ7p',host='sql12.freemysqlhosting.net',database='sql12229537')
					''' Load variables '''
					entity, value = wit_response(messaging_text)
					#if questMode == 1:
						
					if messaging_text == "Hello":
						response = "Hello there, I'm Mitra, should we start now?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q1_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q1_no'
										}
									]
						bot.send_button_message(sender_id,response,buttons)
						#bot.send_text_message(sender_id, response)
				elif 'postback' in messaging_event:
					payload_name = messaging_event['postback']['payload']
					if payload_name == "q1_yes":
						response = "Do you have any conerns about your future?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q2_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q2_no'
										}
									]
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q1_no":
						response = "Have a great day then!"
						bot.send_text_message(sender_id, response)
					elif payload_name == "q2_yes":
						response = "Do you have low self esteem?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q3_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q3_no'
										}
									] 
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q3_yes" or payload_name == "q3_no":
						response = "Do you feel like you have lack of self confidence?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q4_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q4_no'
										}
									]
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q4_yes" or payload_name == "q4_no":
						response = "Are you afraid of facing changes in life?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q5_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q5_no'
										}
									]
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q5_yes" or payload_name == "q5_no":
						response = "Does outside competition affect your performance?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q6_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q6_no'
										}
									]
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q6_yes" or payload_name == "q6_no":
						response = "Do you have exam fear?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q7_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q7_no'
										}
									]
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q2_no":
						response = "Do you have exam fear?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q7_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q7_no'
										}
									]
						bot.send_button_message(sender_id,response,buttons)	

	return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()

if __name__=="__main__":
   app.run(debug=True,port=80)
