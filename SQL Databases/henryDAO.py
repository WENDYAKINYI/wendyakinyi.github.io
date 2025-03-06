import mysql.connector
from henryInterfaceClasses import Author, Book


class HenryDAO:
    def __init__(self):
        try:

            # Establish the connection when the DAO is created
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Mogad1shu*#",
                database="comp3421"
            )
            self.cursor = self.conn.cursor()
        # Check if the connection is established
            print("Database connection established successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def get_author_data(self):
        # Query to get author data
        query = """
        SELECT AUTHOR_NUM, AUTHOR_LAST, AUTHOR_FIRST 
        FROM HENRY_AUTHOR 
        WHERE EXISTS (SELECT 1 FROM HENRY_WROTE WHERE HENRY_WROTE.AUTHOR_NUM = HENRY_AUTHOR.AUTHOR_NUM)
        """
        print(f"Executing query: {query}")  # Print the query
        self.cursor.execute(query)
        authors = []
        for (author_num, last_name, first_name) in self.cursor:
            authors.append(Author(author_num, last_name, first_name))
        return authors

    def get_books_by_author(self, author_num):
        # Query to get books written by the selected author
        query = """
        SELECT HENRY_BOOK.BOOK_CODE, TITLE, PRICE 
        FROM HENRY_BOOK 
        JOIN HENRY_WROTE ON HENRY_BOOK.BOOK_CODE = HENRY_WROTE.BOOK_CODE 
        WHERE HENRY_WROTE.AUTHOR_NUM = %s
        """
        print(f"Executing query: {query} with author_num: {
              author_num}")  # Print the query with parameter
        self.cursor.execute(query, (author_num,))
        books = []
        for (book_code, title, price) in self.cursor:
            books.append(Book(book_code, title, price))
        return books

    def get_books_by_category(self, category):
        # Query to get books by category
        query = """
        SELECT BOOK_CODE, TITLE, PRICE 
        FROM HENRY_BOOK 
        WHERE TYPE = %s
        """
        print(f"Executing query: {query} with category: {
              category}")  # Print the query with parameter
        self.cursor.execute(query, (category,))
        books = []
        for (book_code, title, price) in self.cursor:
            books.append(Book(book_code, title, price))
        return books

    def get_books_by_publisher(self, publisher_name):
        # Query to get books by publisher
        query = """
        SELECT HENRY_BOOK.BOOK_CODE, TITLE, PRICE 
        FROM HENRY_BOOK 
        JOIN HENRY_PUBLISHER ON HENRY_BOOK.PUBLISHER_CODE = HENRY_PUBLISHER.PUBLISHER_CODE
        WHERE HENRY_PUBLISHER.PUBLISHER_NAME = %s
        """
        self.cursor.execute(query, (publisher_name,))
        books = []
        for (book_code, title, price) in self.cursor:
            books.append(Book(book_code, title, price))
        return books

    def get_branch_info_by_book(self, book_code):
        # Query to get branch inventory for a specific book
        query = """
        SELECT HENRY_BRANCH.BRANCH_NAME, HENRY_INVENTORY.ON_HAND 
        FROM HENRY_BRANCH
        JOIN HENRY_INVENTORY ON HENRY_BRANCH.BRANCH_NUM = HENRY_INVENTORY.BRANCH_NUM
        WHERE HENRY_INVENTORY.BOOK_CODE = %s
        """
        print(f"Executing query: {query} with book_code: {
              book_code}")  # Print the query with parameter
        self.cursor.execute(query, (book_code,))
        branch_info = []
        for (branch_name, on_hand) in self.cursor:
            branch_info.append((branch_name, on_hand))
        return branch_info

    def get_distinct_categories(self):

        query = """
            SELECT DISTINCT TYPE
            FROM HENRY_BOOK
            """
        print(f"Executing query: {query}")
        self.cursor.execute(query)
        categories = [row[0] for row in self.cursor.fetchall()]
        return categories

    def get_all_publishers(self):

        query = """
            SELECT PUBLISHER_NAME
            FROM HENRY_PUBLISHER
            """
        print(f"Executing query: {query}")
        self.cursor.execute(query)
        publishers = [row[0] for row in self.cursor.fetchall()]
        return publishers

    def close(self):
        # Close the database connection when the GUI is closed
        self.cursor.close()
        self.conn.close()


# if __name__ == "__main__":
#     # Test the DAO functionality
#     dao = HenryDAO()

#     # Test get_author_data()
#     print("Testing get_author_data:")
#     authors = dao.get_author_data()
#     for author in authors:
#         print(f"Author: {author}")

#     # Test get_books_by_author with a valid author number
#     print("\nTesting get_books_by_author with author_num = 1:")
#     books = dao.get_books_by_author(1)
#     for book in books:
#         print(f"Book: {book}")

#     # Close the DAO connection
#     dao.close()
