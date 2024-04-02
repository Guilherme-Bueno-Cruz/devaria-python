from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Usuario(BaseModel):
    name: str
    usuario: Optional[str] = None
    senha: str




@app.post("/api/login")
def login(usuario: Usuario):
    if usuario.usuario == 'filipe' and usuario.senha == '123abc':
        resposta = {
            "mensagem": "Login realizado com sucesso"
        }
    else:
        resposta = {
            "mensagem": "Usuário ou senha incorretos"
        }
    return resposta







@app.get("/ola-mundo")
def read_root():
    return {
      "mensagem": "Olá mundo, essa é minha primeira API"
    }

@app.get("/api/soma")
def soma():
    return {
        "resultado": 2 + 3
    }

