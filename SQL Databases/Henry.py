import tkinter as tk
from tkinter import ttk
from henryDAO import HenryDAO


class HenryBookstoreApp:
    def __init__(self, root):
        root.title("Henry Bookstore")
        root.geometry("800x600")

        # Create Notebook
        self.notebook = ttk.Notebook(root)

        # Create frames for each tab
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.tab1, text='Search by Author')
        self.notebook.add(self.tab2, text='Search by Category')
        self.notebook.add(self.tab3, text='Search by Publisher')

        self.notebook.pack(expand=1, fill='both')

        # Initialize HenryDAO (keeps connection open)
        self.dao = HenryDAO()

        # Initialize each tab's class
        HenrySBA(self.tab1, self.dao)
        HenrySBC(self.tab2, self.dao)
        HenrySBP(self.tab3, self.dao)

        # Ensures the database connection is closed when the window is closed
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.dao.close()  # Close the DAO connection
        root.destroy()


# Search by Author Tab
class HenrySBA:
    def __init__(self, frame, dao):
        self.dao = dao
        self.authors = self.dao.get_author_data()
        self.books = []

        # Author Combobox
        label_author = tk.Label(frame, text="Author Selection:")
        label_author.pack(pady=10)
        self.author_combobox = ttk.Combobox(frame, values=self.authors)
        self.author_combobox.bind("<<ComboboxSelected>>", self.author_selected)
        self.author_combobox.pack()

        # Book Combobox
        label_book = tk.Label(frame, text="Book Selection:")
        label_book.pack(pady=10)
        self.book_combobox = ttk.Combobox(frame)
        self.book_combobox.bind("<<ComboboxSelected>>", self.book_selected)
        self.book_combobox.pack()

        # Price Label
        self.price_label = tk.Label(frame, text="Price: $0.00")
        self.price_label.pack(pady=10)

        # TreeView for Branch Information
        self.tree = ttk.Treeview(frame, columns=(
            'Branch', 'Copies Available'), show='headings')
        self.tree.heading('Branch', text='Branch Name')
        self.tree.heading('Copies Available', text='Copies Available')
        self.tree.pack()

        # Automatically select the first author when the GUI starts
        if self.authors:
            self.author_combobox.current(0)
            self.author_selected(None)

    def author_selected(self, event):
        selected_index = self.author_combobox.current()
        selected_author = self.authors[selected_index]

        # Fetch books by the selected author from the DAO
        self.books = self.dao.get_books_by_author(selected_author.author_num)

        # Update the book Combobox
        self.book_combobox["values"] = self.books
        if self.books:
            self.book_combobox.current(0)
            self.book_selected(None)

    def book_selected(self, event):
        selected_index = self.book_combobox.current()
        selected_book = self.books[selected_index]

        # Update price label
        self.price_label.config(text=f"Price: ${selected_book.price:.2f}")

        # Fetch branch info by the selected book from the DAO
        branch_info = self.dao.get_branch_info_by_book(selected_book.book_code)

        # Update the TreeView with the branch info
        self.clear_branch_info()
        for branch, copies in branch_info:
            self.tree.insert('', 'end', values=(branch, copies))

    def clear_branch_info(self):
        # Clear the TreeView before adding new data
        for item in self.tree.get_children():
            self.tree.delete(item)


# Search by Category Tab
class HenrySBC:
    def __init__(self, frame, dao):
        self.dao = dao
        self.books = []
        categories = self.get_categories()

        # Category Combobox
        label_category = tk.Label(frame, text="Category Selection:")
        label_category.pack(pady=10)
        self.category_combobox = ttk.Combobox(
            frame, values=self.get_categories())
        self.category_combobox.bind(
            "<<ComboboxSelected>>", self.category_selected)
        self.category_combobox.pack()

        # Book Combobox
        label_book = tk.Label(frame, text="Book Selection:")
        label_book.pack(pady=10)
        self.book_combobox = ttk.Combobox(frame)
        self.book_combobox.bind("<<ComboboxSelected>>", self.book_selected)
        self.book_combobox.pack()

        # Price Label
        self.price_label = tk.Label(frame, text="Price: $0.00")
        self.price_label.pack(pady=10)

        # TreeView for Branch Information
        self.tree = ttk.Treeview(frame, columns=(
            'Branch', 'Copies Available'), show='headings')
        self.tree.heading('Branch', text='Branch Name')
        self.tree.heading('Copies Available', text='Copies Available')
        self.tree.pack()

    def get_categories(self):
        # Fetch the list of categories from the DAO
        return self.dao.get_distinct_categories()

    def category_selected(self, event):
        selected_category = self.category_combobox.get()
        self.books = self.dao.get_books_by_category(selected_category)
        self.book_combobox["values"] = self.books

        # Automatically select the first book when category changes
        if self.books:
            self.book_combobox.current(0)
            self.book_selected(None)

    def book_selected(self, event):
        selected_index = self.book_combobox.current()

        if selected_index >= 0:  # Ensure an actual book is selected
            selected_book = self.books[selected_index]

            # Update price label with the selected book's price
            self.price_label.config(text=f"Price: ${selected_book.price:.2f}")

            # Fetch branch info by the selected book from the DAO
            branch_info = self.dao.get_branch_info_by_book(
                selected_book.book_code)

            # Update the TreeView with the branch info
            self.clear_branch_info()
            for branch, copies in branch_info:
                self.tree.insert('', 'end', values=(branch, copies))

    def clear_branch_info(self):
        for item in self.tree.get_children():
            self.tree.delete(item)


# Search by Publisher Tab
class HenrySBP:
    def __init__(self, frame, dao):
        self.dao = dao
        self.books = []

        publishers = self.get_publishers()

        # Publisher Combobox
        label_publisher = tk.Label(frame, text="Publisher Selection:")
        label_publisher.pack(pady=10)
        self.publisher_combobox = ttk.Combobox(
            frame, values=self.get_publishers())
        self.publisher_combobox.bind(
            "<<ComboboxSelected>>", self.publisher_selected)
        self.publisher_combobox.pack()

        # Book Combobox
        label_book = tk.Label(frame, text="Book Selection:")
        label_book.pack(pady=10)
        self.book_combobox = ttk.Combobox(frame)
        self.book_combobox.pack()

        # Price Label
        self.price_label = tk.Label(frame, text="Price: $0.00")
        self.price_label.pack(pady=10)

        # TreeView for Branch Information
        self.tree = ttk.Treeview(frame, columns=(
            'Branch', 'Copies Available'), show='headings')
        self.tree.heading('Branch', text='Branch Name')
        self.tree.heading('Copies Available', text='Copies Available')
        self.tree.pack()

    def get_publishers(self):
        # Fetch the list of publishers from the DAO
        return self.dao.get_all_publishers()

    def publisher_selected(self, event):
        selected_publisher = self.publisher_combobox.get()
        self.books = self.dao.get_books_by_publisher(selected_publisher)
        self.book_combobox["values"] = self.books

        # Automatically select the first book when publisher changes
        if self.books:
            self.book_combobox.current(0)
            self.book_selected(None)

    def book_selected(self, event):
        selected_index = self.book_combobox.current()
        selected_book = self.books[selected_index]

        # Update price label
        self.price_label.config(text=f"Price: ${selected_book.price:.2f}")

        # Fetch branch info by the selected book from the DAO
        branch_info = self.dao.get_branch_info_by_book(selected_book.book_code)

        # Update the TreeView with the branch info
        self.clear_branch_info()
        for branch, copies in branch_info:
            self.tree.insert('', 'end', values=(branch, copies))

    def clear_branch_info(self):
        for item in self.tree.get_children():
            self.tree.delete(item)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HenryBookstoreApp(root)
    root.mainloop()
