from twilio.rest import Client
from dotenv import load_dotenv 
import os
from test.py import enviar_sms


load_dotenv()

# Sua conta SID e auth token do Twilio
account_sid = os.getenv('ACCOUNT_SID1')
auth_token = os.getenv('AUTH_TOKEN1')


client = Client(account_sid, auth_token)


mensagem_sid = enviar_sms()


mensagem = client.messages(mensagem_sid).fetch()


status = mensagem.status
print(f'Status da mensagem: {status}')

