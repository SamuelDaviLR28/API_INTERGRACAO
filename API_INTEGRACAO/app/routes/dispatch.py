from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from app.database import get_connection



router = APIRouter()

class VolumeModel(BaseModel):
    volume_id: str
    peso: float
    largura: float
    altura: float
    profundidade: float

class DispatchModel(BaseModel):
    pedido_id: str = Field(..., example="123456")
    awb: str = Field(..., example="AWB123456789")
    remetente: str = Field(..., example="Empresa A")
    destinatario: str = Field(..., example="Cliente B")
    data_prevista: str = Field(..., example="2025-05-15")
    volumes: List[VolumeModel]

@router.post("/dispatch")
def receber_dispatch(dados: DispatchModel):
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Erro de conexão com o banco de dados")
    
    try:
        cursor = conn.cursor()

       
        cursor.execute("""
            INSERT INTO pedidos (pedido_id, awb, remetente, destinatario, data_prevista)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            dados.pedido_id,
            dados.awb,
            dados.remetente,
            dados.destinatario,
            dados.data_prevista
        ))

        pedido_db_id = cursor.lastrowid

       
        for volume in dados.volumes:
            cursor.execute("""
                INSERT INTO volumes (pedido_id, volume_id, peso, largura, altura, profundidade)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                pedido_db_id,
                volume.volume_id,
                volume.peso,
                volume.largura,
                volume.altura,
                volume.profundidade
            ))

        conn.commit()
        return {"status": "success", "message": "Pedido recebido com sucesso"}
    
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao salvar dados: {str(e)}")
    
    finally:
        cursor.close()
        conn.close()
