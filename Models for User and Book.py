import bcrypt
from db import get_db_connection

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (self.username, self.password))
        conn.commit()
        conn.close()

    @staticmethod
    def authenticate(username, password):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()
        if user and bcrypt.checkpw(password.encode(), user['password'].encode()):
            return True
        return False

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (self.title, self.author))
        conn.commit()
        conn.close()

    @staticmethod
    def list_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        conn.close()
        return books

    @staticmethod
    def borrow_book(book_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE books SET available = 0 WHERE id = ?', (book_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def return_book(book_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE books SET available = 1 WHERE id = ?', (book_id,))
        conn.commit()
        conn.close()
