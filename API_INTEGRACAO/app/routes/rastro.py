from fastapi import APIRouter, Depends
from app.auth import verify_token


router = APIRouter(prefix="/rastro", tags=["Rastro"])

@router.post("/", dependencies=[Depends(verify_token)])
async def track_occurrence(data: dict):
    # Aqui vai a lógica de rastreamento de ocorrências
    return {"mensagem": "Ocorrência rastreada com sucesso"}
