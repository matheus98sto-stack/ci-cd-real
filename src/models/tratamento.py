from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from src.config.database import Base

class HistoricoTratamento(Base):
    """Representa o histórico de cálculos de produtos para tratamento da piscina."""
    __tablename__ = "historico_tratamentos"
    
    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime, default=datetime.utcnow)
    volume_litros = Column(Float)
    cloro_g = Column(Float)
    soda_ash_g = Column(Float)
    floculante_ml = Column(Float)