import sqlite3
import models

def create_connection():
    connection = sqlite3.Connection("movies.db")
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies
    (
    id integer primary key autoincrement, 
    title text not null, 
    director text not null
    )''')
    connection.commit()
    connection.close()

create_table()

def create_movie(movie: models.MovieCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''Insert into movies(title, director) values (?, ?)''',(movie.title, movie.director))
    connection.commit()
    movie_id = cursor.lastrowid
    connection.close()
    return movie_id

def read_movie():
    #get all movies
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    movies = [models.Movie(id=row[0], title=row[1], director=row[2]) for row in rows]
    print(movies)
    connection.close()
    return movies

def read_movie(movie_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies WHERE id=?", (movie_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return models.Movie(id=row[0], title=row[1], director=row[2])

def update_movie(movie_id: int, movie: models.Movie):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''Update movies set title=?, director=?, where id=?''', (movie.title, movie.director, movie_id))
    connection.commit()
    update = cursor.rowcount
    connection.close()
    return update>0

def delete_movie(movie_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM movies WHERE id=?", (movie_id))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted>0