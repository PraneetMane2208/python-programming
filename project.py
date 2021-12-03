class library:

    def __init__(self,listofbooks) :
        self.books=listofbooks
        pass

    def displayAvailableBooks(self):
        print("books present in the libray are :  ")
        for book in self.books:
            print(book)

    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"you have issued {bookname} and please keep it safe")
            self.books.remove(bookname)
        else:
            print(f"sorry {bookname} is not present or issued by someone else ")

    def returnBook(self,bookname):
        self.books.append(bookname)
        print("thanks")

class student:
    def requestBook(self):
        self.book=input("enter the book name which you want  :")
        return self.book

    def returnBook(self):
        self.book=input("enter the book you want to return :")

if __name__=="__main__":
    centralLibrary=library(["hcv","dcpandey","oswal","chengiz khan","mtg","sultan"])
    # centralLibrary.displayAvailableBooks()

    while(True):
        welcomMsg='''welcome to central library
        please choose an option:
        1.listing all books
        2.Request a book
        3.Return a book
        4.exit the central library  '''
        print(welcomMsg)

        a=int(input("enter your choice :  "))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook(self))
        elif a==3:
            centralLibrary.returnBook(student.returnBook('self'))
        elif a==4:
            exit()
        
        else:
            print("invalid choice")
        