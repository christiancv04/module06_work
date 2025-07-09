from pydantic import BaseModel
from datetime import date


class Movie(BaseModel):
    autor: str
    descripcion: str
    fecha_estreno: date


class MovieResponse(BaseModel):
    message: str
    data: Movie
