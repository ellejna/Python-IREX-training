from fastapi import FastAPI, HTTPException
from typing import List
import models
import database


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to movies CRUD API"}

@app.post("/movies/", response_model=models.Movie)
def create_movie(movie: models.MovieCreate):
    movie_id = database.create_movie(movie)
    return models.Movie(id=movie_id, **movie.dict())

@app.get("/movies/", response_model=List[models.Movie])
def create_movie():
    return database.read_movie()

@app.get("/movies/{movie_id}", response_model=models.Movie)
def read_movie(movie_id: int):
    movie = database.read_movie(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, deetail="Movie not found")
    return movie

@app.put("/movies/{movie_id}", response_model=models.Movie)
def read_movie(movie_id: int, movie: models.MovieCreate):
    update = database.update_movie(movie_id, movie)
    if not update:
        raise HTTPException(status_code=404, detail="Movie not found")
    return models.Movie(id=movie_id, **movie.dict())

@app.delete("/movies/{movie_id}", response_model=dict)
def delete_movie(movie_id: int):
    deleted = database.delete_movie(movie_id)
    if not deleted:
        raise HTTPSException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted successfully"}

