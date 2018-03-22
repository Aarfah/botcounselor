from wit import Wit

access_token = "EUA3JSXFPYHAF676JKSOJHUM6KJSSUTO"

#creation of wit.ai client
client = Wit(access_token = access_token)


'''message_text ="I had a good day"
resp = client.message(message_text)
print(resp) '''

def wit_response(message_text):
	resp = client.message(message_text)
	entity = None
	value = None

	try:
		entity = list(resp['entities'])[0]
		value = resp['entities'][entity][0]['value']
	except:
		pass
	return(entity, value)

#print(wit_response("I had a good day"))
