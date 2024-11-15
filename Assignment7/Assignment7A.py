"""
Class:      CSE1321L
Section:    Module 6
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 7A
"""

class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed


    def borrow(self):
        if self.is_borrowed:
            return "Book already borrowed"

        self.is_borrowed = True
        return "You borrowed the book"


    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return "You returned the book"

        return "Book is not borrowed"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            return "Borrow limit reached"

        if book in self.borrowed_books:
            return "Book already borrowed by this member"
        else:
            if book.is_borrowed:
                return "Book already borrowed by someone else"
            else:
                book.borrow()
                self.borrowed_books.append(book)
                return "Book borrowed successfully"


    def return_book(self, book):
        if book not in self.borrowed_books:
            return "Book not borrowed by this member"
        else:
            book.return_book()
            self.borrowed_books.remove(book)
            return "Book returned successfully"


# Testing

# Define a Book and Member for testing
book1 = Book("1984", "George Orwell")
member1 = Member("Alice")
# Scenario 1: Alice borrows the book "1984"
print(member1.borrow_book(book1))

# Output: "Book borrowed successfully"
# Scenario 2: Alice tries to borrow "1984" again

print(member1.borrow_book(book1))
# Output: "Book already borrowed by this member"
# Scenario 3: Alice returns "1984"

print(member1.return_book(book1))
# Output: "Book returned successfully"
# Scenario 4: Alice tries to return "1984" again (after already returning it)

print(member1.return_book(book1))
# Output: "Book not borrowed by this member"
# Scenario 5: Another member, Bob, tries to borrow "1984" after Alice has returned it

member2 = Member("Bob")
print(member2.borrow_book(book1))
# Output: "Book borrowed successfully"
# Scenario 6: Alice tries to borrow more than the limit of 3 books

#Define more books
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Catcher in the Rye", "J.D. Salinger")
book4 = Book("Pride and Prejudice", "Jane Austen")

# Alice borrows 3 books
print(member1.borrow_book(book2))
# Output: "Book borrowed successfully"

print(member1.borrow_book(book3))
# Output: "Book borrowed successfully"

print(member1.borrow_book(book4))
# Output: "Book borrowed successfully"

book5 = Book("The Art of War", "Sun Tzu")

# Alice tries to borrow a fourth book
print(member1.borrow_book(book5))
# Output: "Borrow limit reached"