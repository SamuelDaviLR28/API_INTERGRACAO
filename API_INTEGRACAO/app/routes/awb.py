from fastapi import APIRouter, Query
from app.database import get_connection


router = APIRouter()

@router.get("/awb/consulta")
def consulta_awb(awb: str = Query(...)):
    conn = get_connection()
    if not conn:
        return {"status": "error", "message": "Erro ao conectar com o banco de dados"}

    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT id, awb, filename, uploaded_at FROM comprovantes_entrega WHERE awb = %s ORDER BY uploaded_at DESC",
        (awb,)
    )
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    if not resultados:
        return {"status": "not_found", "message": f"Nenhum comprovante encontrado para AWB {awb}"}

    return {"status": "success", "awb": awb, "comprovantes": resultados}
