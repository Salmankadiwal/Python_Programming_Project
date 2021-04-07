from datetime import date,datetime

class Library:

    def __init__(self,librarybooks):
        self.books = librarybooks

    def displaybooks(self):
        print("The available books at the library are : ",end="")
        for books in self.books:
            print("\n ***",books,end="")

    def borrowbooks(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname} and make sure you return it on time.")
            self.books.remove(bookname)
        else:
            print(f"Sorry the book {bookname} is currently not available.")

    def returnbooks(self, bookname):
        self.books.append(bookname)
        print(f"Thanks for returning the book  {bookname}.")
        print("See you again...Thanks for borrowing and returning the book.")

class Student:

    a = date.today()
    now = datetime.now()


    def __init__(self,name):
        self.name = name

    def borrowedtime(self):
        print(f'The Student {self.name} has borrowed the book {self.bo} on {self.a} at {self.now.strftime("%I:%M:%S %p")}')

    def returnedtime(self):
        print(f'The Student {self.name} has returneded the book {self.bo} on {self.a} at {self.now.strftime("%I:%M:%S %p")}')

    def requestbook(self):
        self.bo = input("What book you wanna request for ? ")
        self.borrowedtime()
        return self.bo


    def returnbook(self):
        self.bo = input("What book you wanna return ?")
        self.returnedtime()
        return self.bo



if __name__ == '__main__':

    ReginaLibrary = Library(["Java","Algorithm","Pandas","Python"])
    student1 = Student("Salman")
    #ReginaLibrary.displaybooks()

while(True):
    print()
    print('''
    =====WELCOME TO REGINALIBRARY=====
         Please Choose an option : 
         1. To display all books
         2. Request a book
         3. Return a book
         4. Exit the Library''')

    print()
    a = int(input("Enter your choice :"))

    if a == 1:
        ReginaLibrary.displaybooks()
    elif a == 2:
        ReginaLibrary.borrowbooks(student1.requestbook())
    elif a == 3:
        ReginaLibrary.returnbooks(student1.returnbook())
    elif a == 4:
         exit()
    else:
        print("Invalid option")

