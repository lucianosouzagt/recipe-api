from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Carrega variáveis do .env
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# Modelo SQLAlchemy
class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)

# Cria tabelas
Base.metadata.create_all(bind=engine)

# Esquema Pydantic
class RecipeCreate(BaseModel):
    title: str
    description: str = None

class RecipeRead(RecipeCreate):
    id: int

app = FastAPI(title="API de Cadastro de Receitas")

@app.post("/recipes/", response_model=RecipeRead)
def create_recipe(payload: RecipeCreate):
    db = SessionLocal()
    recipe = Recipe(**payload.dict())
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    db.close()
    return recipe

@app.get("/recipes/", response_model=List[RecipeRead])
def list_recipes():
    db = SessionLocal()
    recipes = db.query(Recipe).all()
    db.close()
    return recipes

# Rota de teste / health check
@app.get("/", tags=["Test"])
def ping():
    return {"message": "API de receitas criadas com sucesso!!"}