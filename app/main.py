# app/main.py
from fastapi import FastAPI

# Instância da aplicação FastAPI
app = FastAPI(
    title="Recipe API",
    description="API para gerenciar receitas de culinária",
    version="0.1.0",
)

@app.get("/")
async def read_root():
    """
    Endpoint de teste para verificar se a API está funcionando.
    """
    return {"message": "Bem-vindo à API de Receitas! O ambiente está configurado com sucesso."}

@app.get("/health")
async def health_check():
    """
    Endpoint de health check para verificar a saúde da aplicação.
    """
    return {"status": "ok"}