import os
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from dotenv import load_dotenv 

app = FastAPI()

@app.post("/enviar-dados")
async def enviar_dados(numero: str = Form(...), texto: str = Form(...)):
    
    
    return JSONResponse(content={"numero_recebido": numero, "texto_recebido": texto})






