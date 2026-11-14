class Boook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - Status: {status}"


book1 = Boook("Harry Potter", "J.K. Rowling")
book2 = Boook("1984", "George Orwell")

print(book1)
print(book2)

book1.borrow()
book1.borrow()

print(book1)

book1.return_book()
book2.return_book()

print(book1)
print(book2)