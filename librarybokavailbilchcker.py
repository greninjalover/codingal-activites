books = ["Harry Potter", "The Hobbit", "Matilda", "Diary of a Wimpy Kid"]
copies = [3, 0, 5, 2]

library = {book: copy for book, copy in zip(books, copies)}

print("Library Book Availability Checker")
print()

available_books = [book for book in books if library[book] > 0]

print("Available books:")
for book in available_books:
    print(book)

print()

late_fees = [2, 4, 6, 8]
new_fees = list(map(lambda fee: fee + 1, late_fees))

print("Updated late fees:")
print(new_fees)

print()

book_choice = input("Enter a book name: ")

if library.get(book_choice, 0) == 0:
    print("Sorry, that book is unavailable.")
    exit()

print("Good news! The book is available.")
print("Copies available:", library[book_choice])