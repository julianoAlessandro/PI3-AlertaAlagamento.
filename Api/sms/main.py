from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/enviar-numero")
async def enviar_numero(numero: str):    
    # Faça algo com o número, se necessário
    
    return JSONResponse(content={"numero_recebido": numero})
