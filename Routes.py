from fastapi import APIRouter
from Models.Movie import Movie
from Models.Movie import MovieResponse
from Controllers import MovieController

router = APIRouter()


@router.get("/movies")
def get_movies():
    return MovieController.get_movies()


@router.post("/movies", response_model=MovieResponse)
def create_movie(movie: Movie):
    MovieController.create_movie(movie)
    return {"message": "Película agregada correctamente", "data": movie}


@router.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: Movie):
    MovieController.update_movie(movie_id, movie)
    return {"message": "Película actualizada"}


@router.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    MovieController.delete_movie(movie_id)
    return {"message": "Película eliminada"}
