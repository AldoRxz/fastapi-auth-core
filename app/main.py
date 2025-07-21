from fastapi import FastAPI
from app.api.routes import auth
from app.db.models import Base
from app.db.session import engine

app = FastAPI(
    title="FASTAPI AUTH SERVICE",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Crear tablas al iniciar la app
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# Rutas de autenticación
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
