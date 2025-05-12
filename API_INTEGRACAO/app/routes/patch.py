from fastapi import APIRouter, Depends
from app.auth import verify_token


router = APIRouter(prefix="/patch", tags=["Patch"])

@router.patch("/", dependencies=[Depends(verify_token)])
async def update_patch(data: dict):
      return {"mensagem": "Patch atualizado com sucesso"}
