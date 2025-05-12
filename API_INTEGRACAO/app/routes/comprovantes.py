from fastapi import APIRouter, UploadFile, File, Form
from datetime import datetime
import os
from pathlib import Path

from app.database import get_connection

router = APIRouter()

UPLOAD_DIR = Path("uploads/comprovantes")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/comprovante/upload")
async def upload_comprovante(awb: str = Form(...), file: UploadFile = File(...)):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{awb}_{timestamp}_{file.filename}"
    filepath = UPLOAD_DIR / filename

    with open(filepath, "wb") as f:
        content = await file.read()
        f.write(content)

    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO comprovantes_entrega (awb, filename) VALUES (%s, %s)",
            (awb, filename)
        )
        conn.commit()
        cursor.close()
        conn.close()

    return {
        "status": "success",
        "message": "Comprovante salvo com sucesso.",
        "filename": filename
    }
