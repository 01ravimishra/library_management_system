import sqlite3
from prettytable import PrettyTable

# Connect to SQLite database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create books table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL
)
''')
conn.commit()

def add_book(title, author, year):
    cursor.execute('''
    INSERT INTO books (title, author, year)
    VALUES (?, ?, ?)
    ''', (title, author, year))
    conn.commit()

def view_books():
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    table = PrettyTable()
    table.field_names = ["ID", "Title", "Author", "Year"]
    for row in rows:
        table.add_row(row)
    print(table)

def delete_book(book_id):
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter publication year: "))
            add_book(title, author, year)
            print("Book added successfully!")

        elif choice == '2':
            print("Current Books in Library:")
            view_books()

        elif choice == '3':
            book_id = int(input("Enter the ID of the book to delete: "))
            delete_book(book_id)
            print("Book deleted successfully!")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
