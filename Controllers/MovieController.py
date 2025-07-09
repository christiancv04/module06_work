import psycopg2
from fastapi import HTTPException
from Models import Movie

db_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": "5432",
}


def get_movies():
    try:
        conn = psycopg2.connect(**db_params)
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM my_movies")
            rows = cursor.fetchall()
            return [
                {
                    "id": r[0],
                    "autor": r[1],
                    "descripcion": r[2],
                    "fecha_estreno": r[3].isoformat(),
                }
                for r in rows
            ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def create_movie(movie: Movie):
    try:
        conn = psycopg2.connect(**db_params)
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO my_movies (autor, descripcion, fecha_estreno)
                VALUES (%s, %s, %s)
            """,
                (movie.autor, movie.descripcion, movie.fecha_estreno),
            )
            conn.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def update_movie(movie_id: int, movie: Movie):
    try:
        conn = psycopg2.connect(**db_params)
        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE my_movies
                SET autor = %s, descripcion = %s, fecha_estreno = %s
                WHERE id = %s
            """,
                (movie.autor, movie.descripcion, movie.fecha_estreno, movie_id),
            )
            conn.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def delete_movie(movie_id: int):
    try:
        conn = psycopg2.connect(**db_params)
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM my_movies WHERE id = %s", (movie_id,))
            conn.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
