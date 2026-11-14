class Book():
    def __init__(self, title, author, isborrowed):
        self.title=title
        self.author=author
        self.isborrowed=False

    def borrow(isborrowed):
        isborrowed=True
        print("The book has been borrowed")

    def returrn(isborrowed):
        isborrowed=False
        print("The book has been returned")

book1=Book("Harry potter")
book1.borrow
book1.returrn
