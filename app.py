import os, sys
from flask import Flask, request
from utils import wit_response
from pymessenger import Bot

#initialise Flask app
app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAFGnmzStNcBAIVibLcyq18ZBXpgoNeeQSDhYq9qjcKiIGkvtEZB0ZCUVGyxuYg5bl6qeYiJB9apFXem2A1C7ZCyKrGHuxEKQsvD85bkXlkmHLCRIwRxyDhEZANMwTxoX6VU2co6Jm6LBpvA3p9a7WF614BgZBzHLOYukYZCzBKutF9TCEH94iv"

bot = Bot(PAGE_ACCESS_TOKEN)



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
					
					response = None
					entity, value = wit_response(messaging_text)
					if messaging_text == "Hello" or "hello" or "hey" or "Hey" or "HELLO" :
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
						if payload_name == "q3_yes":
							sol="Take up aptitude tests in terms of careers"
							bot.send_text_message(sender_id, sol)
							url = "https://www.youtube.com/watch?v=FeLpvgAVtU8"
							bot.send_video_url(sender_id,url)
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
						if payload_name == "q4_yes":
							sol="Mix with people of your own strata initially to increase your self-confidence"
							bot.send_text_message(sender_id,sol)
							url = "https://www.youtube.com/watch?v=llsRkWjM8hU"
							bot.send_video_url(sender_id,url)
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
						if payload_name == "q5_yes":
							sol="one needs to start becoming strong emotionally in order to consider future in terms of family and friends"
							bot.send_text_message(sender_id,sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q6_yes" or payload_name == "q6_no" or payload_name == "q2_no":
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
						if payload_name == "q6_yes":
							sol="Learn from your competitor’s strategies and success instead of getting demotivated."
							bot.send_text_message(sender_id,sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q7_yes":
						response = "Is it external pressure that is worrying you?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q8_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q8_no'
										}
									]
						
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q8_yes" or payload_name == "q8_no":
						response = "Is internal pressure affecting your academic performance?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q9_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q9_no'
										}
									]
						if payload_name == "q8_yes":
							sol=" Have faith in your preparation and don’t get demotivated by others."
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q9_yes" or payload_name == "q9_no":
						response = "Is there a lack of preparation from your side?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q10_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q10_no'
										}
									]
						if payload_name == "q9_yes":
							sol="Do not procrastinate"
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)	
					elif payload_name == "q10_yes" or payload_name == "q10_no" or payload_name == "q7_no":
						response = "Is lack of sleep disturbing your daily life?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q11_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q11_no'
										}
									]
						if payload_name == "q10_yes":
							sol="Do not procrastinate and Manage time well"
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q11_yes":
						response = "Are you suffering from any chronological illness?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q12_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q12_no'
										}
									]
									
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q12_yes" or payload_name == "q12_no":
						response = "Are you facing any sort of work pressure?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q13_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q13_no'
										}
									]
						if payload_name == "q12_yes":
							sol="Consult a doctor"
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q13_yes" or payload_name == "q13_no":
						response = "Are you addicted to say, social media?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q14_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q14_no'
										}
									]
						if payload_name == "q13_yes":
							sol="Manage time"
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q14_yes" or payload_name == "q14_no" or payload_name == "q11_no":
						response = "Are you having overload at school/college?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q15_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q15_no'
										}
									]
						if payload_name == "q14_yes":
							sol="Set time and frequency limits and follow them rigorously"
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q15_yes":
						response = "Are the environmental factors affecting your performance?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q16_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q16_no'
										}
									]
						
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q16_yes" or payload_name == "q16_no":
						response = "Do you have any health issues?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q17_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q17_no'
										}
									]
						if payload_name == "q16_yes":
							sol="Keep a balance between everything you do"
							bot.send_text_message(sender_id, sol)
						
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q17_yes" or payload_name == "q17_no":
						response = "Do you feel that you're a pessimistic thinker?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q18_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q18_no'
										}
									]
						if payload_name == "q17_yes":
							sol="Consult a doctor and follow the regime prescribed"
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q18_yes" or payload_name == "q18_no":
						response = "Do you feel like you are being less productive lately?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q19_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q19_no'
										}
									]
						if payload_name == "q18_yes":
							sol="one must always have positive attitude towards everything"
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q19_yes" or payload_name == "q19_no" or payload_name == "q15_no":
						response = "Are you concerned about your physical appearance?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q20_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q20_no'
										}
									]
						if payload_name == "q19_yes":
							sol="Be confident and work on your weaknesses to perform well"
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q20_yes":
						response = "Do you compare your appearance with that of celebrities?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q21_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q21_no'
										}
									]
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q21_yes" or payload_name == "q21_no":
						response = "Are you unhappy with your genetics?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q22_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q22_no'
										}
									]
						if payload_name == "q21_yes":
							sol="avoid comparison,increase self esteem, one's own acceptance is necessary!,once accepted, one can work on changing, if they want to. But acceptance is necessary!,its okay to be the way I am kinda attitude should be inculcated!"
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q22_yes" or payload_name == "q22_no":
						response = "Do you feel like you have low self esteem issues?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q23_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q23_no'
										}
									]
						if payload_name == "q22_yes":
							sol="one needs to understand that everyone is different, and everyone has different ways of living life."
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q23_yes" or payload_name == "q23_no" or payload_name == "q20_no":
						response = "Are you afraid to confront your parents in case of conflicts?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q24_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q24_no'
										}
									]
						if payload_name == "q23_yes":
							sol="one's own acceptance is necessary!"
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q24_yes":
						response = "Are you having authority issues?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q25_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q25_no'
										}
									]
						
									
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q25_yes" or payload_name == "q25_no":
						response = "Are you afraid to talk to your parents due to the age gap?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q26_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q26_no'
										}
									]
						if payload_name == "q25_yes":
							sol="Best way is to talk and find a mutual solution."
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q26_yes" or payload_name == "q26_no":
						response = "Do you have low grades?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q27_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q27_no'
										}
									]
						if payload_name == "q26_yes":
							sol="Try to explain your perspective without opposing theirs. "
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q27_yes" or payload_name == "q27_no":
						response = "Do you feel like your potential is being underestimated your parents?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q28_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q28_no'
										}
									]
						if payload_name == "q27_yes":
							sol="Perform self-analysis and do your best "
							bot.send_text_message(sender_id, sol)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q28_yes":
						sol=" Try to inculcate empathy and respect for the elder generation by spending more time with them and understanding their perspectives.  "
						bot.send_text_message(sender_id, sol)
					elif payload_name == "q28_no" or payload_name == "q28_yes":
						sol="Nice talking to you!"
						bot.send_text_message(sender_id, sol)						
	return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()

if __name__=="__main__":
   app.run(debug=True,port=80)
