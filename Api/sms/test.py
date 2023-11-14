from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


account_sid = "AC7b6b626719f6558f48f8edc2962bdf19"
auth_token = "e37c02a0f06be5d7ef7893bc75440ce3"


client = Client(account_sid, auth_token)


from_phone_number = "+12562516513"


to_phone_number = "+5519993620346"  


message_body = "ssss"

if message_body:
    try:
    
        message = client.messages.create(
            body=message_body,
            from_=from_phone_number,
            to=to_phone_number
        )
        
        print(f"SMS enviado com sucesso, SID: {message.sid}")
        
      
        print(f"Status da mensagem: {message.status}")
        
    except TwilioRestException as e:
      
        if e.code == 21211:
            print(f"Não foi possível realizar a operação. Número de telefone inválido.")
        else:
            print(f"Erro ao enviar o SMS: {e.msg}")
else:
    print("O corpo da mensagem está vazio. Não é possível enviar o SMS.")

