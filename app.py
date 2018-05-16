import os, sys
from flask import Flask, request
from utils import wit_response
from pymessenger import Bot

#initialise Flask app
app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAFGnmzStNcBAIVibLcyq18ZBXpgoNeeQSDhYq9qjcKiIGkvtEZB0ZCUVGyxuYg5bl6qeYiJB9apFXem2A1C7ZCyKrGHuxEKQsvD85bkXlkmHLCRIwRxyDhEZANMwTxoX6VU2co6Jm6LBpvA3p9a7WF614BgZBzHLOYukYZCzBKutF9TCEH94iv"

bot = Bot(PAGE_ACCESS_TOKEN)

count_fc=0 #future concerns
count_fe=0 #fear of exams
count_ls=0 #lack of sleep
count_os=0 #overload at school
count_pa=0 #physical appearance
count_pc=0 #confrontation with parents

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
	global count_fc
	global count_fe
	global count_ls
	global count_os
	global count_pa
	global count_pc
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
					if messaging_text == "Hello" or "hello" or "hey" or "Hey" or "HELLO":
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
					elif messaging_text == "Bye" or "bye" or "Got to go":
						'''if count_fc > 4:
							responses = "It looks like you have concerns about your future."
						if count_fe > 2:
							responses += " You seem to have exam fear."
						if count_ls > 2:
							responses += " Lack of sleep might be the issue you are facing."
						if count_os > 4:
							responses = " Don't feel burdened due to overload in school/college work."
						if count_pa > 2:
							responses += " Your concern about your physical appearance might be troubling you."
						if count_pc > 2:
							responses += " It seems like confontation with your parents could be a problem." 	
						count = count_fc+count_pc+count_pa+count_os+count_ls+count_fe
						if count > 15:
							responses = "You are advised to visit the nearest counsellor." '''
						responses = "Okay"
						bot.send_text_message(sender_id, responses)
				elif 'postback' in messaging_event:
					payload_name = messaging_event['postback']['payload']
					if payload_name == "q1_yes": #category-start_yes
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
					
					elif payload_name == "q1_no": #category-start_no
						response = "Have a great day then!"
						bot.send_text_message(sender_id, response)
					
					elif payload_name == "q2_yes": #category-future concerns_yes
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

					elif payload_name == "q3_yes": #subcategory- low self esteem_yes
						#global count_fc
						count_fc+=1
						response = "Are you extremely critical of yourself?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q29_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q29_no'
										}
									]
						sol="Take up aptitude tests in terms of careers.Watch this to feel better!"
							#bot.send_text_message(sender_id, sol)
						buttons1 =	[
										{	
											'type':'web_url',
											'url':'https://www.youtube.com/watch?v=rcTSUwo2EoQ',
											'title':'Video'
										}
									]
						bot.send_button_message(sender_id,sol,buttons1)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q29_yes" or payload_name == "q29_no":
						response = "Do you judge yourself to be inferior compared to your peers?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q30_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q30_no'
										}
									]
						if payload_name == "q29_yes":
							#global count_fc
							count_fc+=1
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q30_yes" or payload_name == "q30_no":
						response = "Do you unnecessarily blame yourself when things go wrong?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q31_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q31_no'
										}
									]
						if payload_name == "q30_yes":
							#global count_fc
							count_fc+=1
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q31_yes" or payload_name == "q3_no" or payload_name == "q31_no":
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
						if payload_name == "q31_yes":
							#global count_fc
							count_fc+=1
						if payload_name == "q3_yes":
							sol="Take up aptitude tests in terms of careers.Watch this to feel better!"
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=rcTSUwo2EoQ',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_fc
							count_fc+=1
							sol="Mix with people of your own strata initially to increase your self-confidence"
							bot.send_text_message(sender_id,sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=CoxOb5ls-sY',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
							#bot.send_video_url(sender_id,url)
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
							#global count_fc
							count_fc+=1
							sol="one needs to start becoming strong emotionally in order to consider future in terms of family and friends"
							#bot.send_text_message(sender_id,sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=MCgTDLtxJzQ',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_fc
							count_fc+=1
							sol="Learn from your competitors strategies and success instead of getting demotivated."
							#bot.send_text_message(sender_id,sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=qnej4B9smV8',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_fe
							count_fe+=1
							sol=" Have faith in your preparation and dont get demotivated by others."
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=D64TZ-wcLCY',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_fe
							count_fe+=1
							sol="Do not procrastinate"
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=QrcmpYtXXSo',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_fe
							count_fe+=1
							sol="Do not procrastinate and Manage time well"
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=b74KHwbAdaI',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_ls
							count_ls+=1
							sol="Consult a doctor and take proper medications!"
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=GYx0DZKth-8',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_ls
							count_ls+=1
							sol="Manage time"
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=IAaeJSGWTZc',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_ls
							count_ls+=1
							sol="Set time and frequency limits and follow them rigorously"
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=CLMnDV3P_uM',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_os
							count_os+=1
							sol="Keep a balance between everything you do"
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=bkk_U9qpi9w',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_os
							count_os+=1
							sol="Consult a doctor and follow the regime prescribed"
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=MsHznlPBBTI',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_os
							count_os+=1
							sol="one must always have positive attitude towards everything"
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=ylAlwtNBopY',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q19_yes":
						#global count_os
						count_os+=1
						response = "Are you being bullied?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q32_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q32_no'
										}
									]
						
						sol="Be confident and work on your weaknesses to perform well"
						#bot.send_text_message(sender_id, sol)
						buttons1 =	[
										{	
											'type':'web_url',
											'url':'https://www.youtube.com/watch?v=gXlIAS-rI4E',
											'title':'Video'
										}
									]
						bot.send_button_message(sender_id,sol,buttons1)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q32_yes" or payload_name == "q32_no":
						response = "Is ragging prevalent in your school/work environment?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q33_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q33_no'
										}
									]
						if payload_name == "q32_yes":
							#global count_os
							count_os+=1
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q33_yes" or payload_name == "q33_no":
						response = "Are you unable to cope up with the subjects taught in school/college?"
						buttons =	[
										{
											'type':'postback',
											'title':'yes',
											'payload':'q34_yes'
										},
										{
											'type':'postback',
											'title':'no',
											'payload':'q34_no'
										}
									]
						if payload_name == "q33_yes":
							#global count_os
							count_os+=1
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q19_no" or payload_name == "q34_yes" or payload_name == "q34_no" or payload_name == "q15_no":
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
						if payload_name == "q34_yes":
							#global count_os
							count_os+=1
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
							#global count_pa
							count_pa+=1
							sol="avoid comparison,increase self esteem, one's own acceptance is necessary!,once accepted, one can work on changing, if they want to. But acceptance is necessary!,its okay to be the way I am kinda attitude should be inculcated!"
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=0MPG-aLD-EY',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_pa
							count_pa+=1
							sol="one needs to understand that everyone is different, and everyone has different ways of living life."
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
										
										{	
											'type':'web_url',
											'url':'https://www.youtube.com/watch?v=N62LMzC2_F0',
											'title':'Video'
										}
									]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_pa
							count_pa+=1
							sol="one's own acceptance is necessary!"
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=KY5TWVz5ZDU',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
							
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
							#global count_pc
							count_pc+=1
							sol="Best way is to talk and find a mutual solution."
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=16-X3tOoIxM',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_pc
							count_pc+=1
							sol="Try to explain your perspective without opposing theirs. "
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=SnHKw3kSk4o',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
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
							#global count_pc
							count_pc+=1
							sol="Perform self-analysis and do your best "
							#bot.send_text_message(sender_id, sol)
							buttons1 =	[
											{	
												'type':'web_url',
												'url':'https://www.youtube.com/watch?v=99bVMixpCJg',
												'title':'Video'
											}
										]
							bot.send_button_message(sender_id,sol,buttons1)
						bot.send_button_message(sender_id,response,buttons)
					elif payload_name == "q28_yes":
						#global count_pc
						count_pc+=1
						sol=" Try to inculcate empathy and respect for the elder generation by spending more time with them and understanding their perspectives.  "
						#bot.send_text_message(sender_id, sol)
						buttons1 =	[
										
										{	
											'type':'web_url',
											'url':'https://www.youtube.com/watch?v=99bVMixpCJg',
											'title':'Video'
										}
									]
						bot.send_button_message(sender_id,sol,buttons1)
					elif payload_name == "q28_no" or payload_name == "q28_yes":
						sol="Nice talking to you!"
						bot.send_text_message(sender_id, sol)
										
	return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()

if __name__=="__main__":
   app.run(debug=True,port=80)