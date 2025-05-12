from fastapi import APIRouter, Depends
from app.auth import verify_token


router = APIRouter(prefix="/motorista", tags=["Motorista"])

@router.post("/", dependencies=[Depends(verify_token)])
async def register_driver(data: dict):
    # Aqui vai a lógica de cadastro do motorista
    return {"mensagem": "Motorista cadastrado com sucesso"}
