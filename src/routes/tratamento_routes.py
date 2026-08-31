from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from src.config.database import get_db
from src.models.tratamento import HistoricoTratamento
from src.services.calculadora import calcular_produtos

router = APIRouter(prefix="/api/piscina", tags=["Tratamento"])

class PiscinaRequest(BaseModel):
    volume_litros: float

@router.post("/calcular-e-salvar")
def calcular_e_salvar(req: PiscinaRequest, db: Session = Depends(get_db)):
    """Calcula a dosagem dos produtos e salva o histórico no banco de dados."""
    produtos = calcular_produtos(req.volume_litros)
    
    novo_tratamento = HistoricoTratamento(
        volume_litros=req.volume_litros,
        cloro_g=produtos["cloro_g"],
        soda_ash_g=produtos["soda_ash_g"],
        floculante_ml=produtos["floculante_ml"]
    )
    
    db.add(novo_tratamento)
    db.commit()
    db.refresh(novo_tratamento)
    
    return {"mensagem": "Salvo com sucesso!", "dados": novo_tratamento}