from fastapi import APIRouter, Depends
from app.auth import verify_token


router = APIRouter(prefix="/cancelar", tags=["Cancelar"])

@router.delete("/", dependencies=[Depends(verify_token)])
async def cancel_delivery(data: dict):
    return {"mensagem": "Entrega cancelada com sucesso"}
