from fastapi import FastAPI
from src.config.database import Base, engine
from src.routes import tratamento_routes
from src.models import tratamento 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Tratamento de Piscina")

app.include_router(tratamento_routes.router)

print('sucesso')