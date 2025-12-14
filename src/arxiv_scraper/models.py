# Arquivo: src/arxiv_scraper/models.py
from typing import List

from pydantic import BaseModel, HttpUrl


class Article(BaseModel):
    """
    Define o esquema de dados para um artigo extraído do Arxiv.
    Usamos Pydantic para garantir a tipagem e validação dos dados.
    """
    arxiv_id: str
    title: str
    authors: List[str]
    subjects: str
    summary: str
    link: HttpUrl # Pydantic valida se é uma URL válida
    submission_date: str

    class Config:
        """Configurações adicionais para o Pydantic."""
        from_attributes = True
