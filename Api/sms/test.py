import os
from main import numero
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv
from fastapi import FastAPI



app=FastAPI()




load_dotenv()

@app.post("/enviar-sms")
def enviar_sms():
    # Obter credenciais da Twilio do ambiente
    account_sid = os.getenv('ACCOUNT_SID1')
    auth_token = os.getenv('AUTH_TOKEN1')

    # Criar cliente Twilio
    client = Client(account_sid, auth_token)

    # Números de telefone
    from_phone_number = "+12562516513"
    to_phone_number = numero

    # Corpo da mensagem
    message_body = "ssss"

    # Verificar se o corpo da mensagem não está vazio
    if message_body:
        try:
            # Enviar mensagem
            message = client.messages.create(
                body=message_body,
                from_=from_phone_number,
                to=to_phone_number
            )

            # Imprimir informações sobre o envio bem-sucedido
            print(f"SMS enviado com sucesso, SID: {message.sid}")
            print(f"Status da mensagem: {message.status}")
            return message.sid  # Retorna o message.sid

        except TwilioRestException as e:
            # Lidar com exceções da Twilio
            if e.code == 21211:
                print(f"Não foi possível realizar a operação. Número de telefone inválido.")
            else:
                print(f"Erro ao enviar o SMS: {e.msg}")

    else:
        # Se o corpo da mensagem estiver vazio
        print("O corpo da mensagem está vazio. Não é possível enviar o SMS.")

# Chama a função ao executar o script
if __name__ == "__main__":
    enviar_sms()


