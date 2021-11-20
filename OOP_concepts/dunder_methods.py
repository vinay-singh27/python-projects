# Special or Dunder methods
'''
Classes in Python can implement certain operations with special method names.
These methods are not actually called directly but by Python specific language syntax
'''


class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


book = Book("The book has no NAME!", "Vinay Singh", 27)

#Special Methods
print(book)
print(len(book))
del book