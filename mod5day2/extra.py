#display books,add books,check out books, check availability
 
class library():
    print("welcome to nadeen's library!")
    def __init__(self,books):
        self.books=books
    def display(self,books):
        print("the current books you can check out are: ")
        for book in self.books:
            print(f"-{books}")
    def checkout(self,book):
        if book in self.books:
            print("you have just checked out a book")
            self.books.remove(book)

        else:
            print("this book is not currently available in the library")

    def return_book(self,book):
        self.books.append(book)
        print("you returned the book, it is now available in the library!")
    def donate(self,book):
        self.books.append(book)
        print("a new book is now available in the library!")
    def __del__(self):
        print('the library is now closed. visit us again tmw.')


l=library(["Biology","The Brothers: Hawthorne","The Inheritence Games"])
l.display()
l.checkout("The Inheritence Games")
l.return_book("The Inheritance Games")
l.donate("Charlie and the Chocolate Factory")