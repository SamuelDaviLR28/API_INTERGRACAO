from fastapi import FastAPI
from app.routes import dispatch, patch, rastro, motorista, rota, cancelar
from app.database import engine, Base
from app import models
from app.routes import comprovante, awb
from dotenv import load_dotenv
import os

app = FastAPI(title="Toutbox Integration API")


Base.metadata.create_all(bind=engine)  


app.include_router(dispatch.router)
app.include_router(patch.router)
app.include_router(rastro.router)
app.include_router(motorista.router)
app.include_router(rota.router)
app.include_router(cancelar.router)
app.include_router(comprovante.router)
app.include_router(awb.router)

load_dotenv()

# Obtenha a variável de ambiente
DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise ValueError("DATABASE_URL não definido no .env")

print("Banco de dados URL carregado com sucesso")