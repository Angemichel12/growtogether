import requests
import random
from django.template.response import TemplateResponse
from users.models import User

token='eyJhbGciOiJub25lIn0.eyJpZCI6ODY0LCJyZXZva2VkX3Rva2VuX2NvdW50IjowfQ.'

headers = {'Authorization': 'Bearer ' + token, 'Content-Type':'application/json'}
# data = {'to' : '+250780614290', 'text' : 'Hello Bella, Your Medical consultatation appointment at Faisal hospital has been approved. This is a test', 'sender' : 'Cimerwa Insurance MGT'}

url = 'https://api.pindo.io/v1/sms/'
# response = requests.post(url, json=data, headers=headers)
# print(response)
# print(response.json())

def send_sms(request, phone):
	text = f'Hello albert, Konti yanyu kuri GrowTogetherSystem yemejwe neza.'
	data = {
        'to':str(phone), 
        'text':text,
        'sender': '_GrowTogetherSystem_'
        }
	response = requests.post(url, json=data, headers=headers)
 
	return response