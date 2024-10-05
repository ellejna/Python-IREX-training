import sqlite3
from venv import create
import requests

from last_day.book_scrapper import authors


def get_db_connection():
    conn = sqlite3.connect("books.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_database():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute('''
    create table if not exists books(
    id integer primary key autoincrement
    title txt, 
    author_id integer, 
    book_link text,
    genres text, 
    average_rating real,
    published_year integer, 
    foreign key (author) references authors(id)
    )
    ''')
    cursor.execute('''
        create table if not exists authors(
        id integer primary key autoincrement, 
        name text unique 
        )
    ''')
    conn.commit()
    return conn, cursor

def insert_author(authors, cursor):
    authors_id={}
    for author in authors:
        cursor.execute('''
            insert opr ignore authors (name)
            values (?)
            )
        ''', (authors,))
        cursor.execute("Select id from authors where name=?", (author,))
        authors_id[author] = cursor.fetchone[0]
    return authors_id

def insert_books(books_dictionary, author_ids, cursor):
    for (title, author), info in books_dictionary.items():
        cursor.execute('''
        insert into books (title, author_id, books_link, genres, average_rating, published_year)
        values (?, ?, ?, ?, ?, ?)
        ''',(
            title,
            author_ids[author],
            info["link"],
            ",".join(info["genres"]), float(info["ave_rating"].split()[0]) if info["ave_rating"] else None,
            int(info["published"].split[0]) if info["published"] else None,
        ))

def insert_data(books_dict, authors):
    conn, cursor = create_database()
    authors_id = insert_author(authors, cursor)
    insert_books(books_dict, authors_id, cursor)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    from book_scrapper import scrape_books

    books_dict, authors = scrape_books()
    insert_data(books_dict, authors)
