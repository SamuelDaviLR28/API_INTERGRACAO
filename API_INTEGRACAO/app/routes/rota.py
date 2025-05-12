from fastapi import APIRouter, Depends
from app.auth import verify_token


router = APIRouter(prefix="/rota", tags=["Rota"])

@router.post("/", dependencies=[Depends(verify_token)])
async def create_route(data: dict):
    # Aqui vai a lógica de criação de rota
    return {"mensagem": "Rota criada com sucesso"}
