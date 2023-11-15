from twilio.rest import Client

# Sua conta SID e auth token do Twilio
account_sid = 'AC7b6b626719f6558f48f8edc2962bdf19'
auth_token = 'be932d0472b06e6ece4625dc99235cad'


client = Client(account_sid, auth_token)


mensagem_sid = 'SM61b27d238b4c0c443e8b8aad1fc6a1f4'


mensagem = client.messages(mensagem_sid).fetch()


status = mensagem.status
print(f'Status da mensagem: {status}')

