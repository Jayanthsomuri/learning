#create a library class
# display book
# lend-book(Who owns the book if not present)
# add book
# return book
# JayLibrary=Library(listbooks, library_name)
#dictionary (books-nameoof person)
#Create a main function and run an infinte while loop asking
#users for their input

class Library:
    def __init__(self,list,name):
        self.bookList = list
        self.name = name
        self.lendDict = {}
    def displayBooks(self):
        print(f"We Having following Books in out library: {self.name}")
        for book in self.bookList:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book databse has been updated.You can take the book now")
        else:
            print(f"Book is already has been used by{self.lendDict[book]}")    
    def addBook(self,book):
        self.bookList.append(book)
        print("Book has been added to the bok list")  
    def returnBook(self,book):
        self.bookList.remove(book)


if __name__ =='__main__':
    jay=Library(['Python','Harry potter','C++','Webdevelopment','Machine learning'],
    'Jscode')
    while(True):
        
        print(f"Welcome to the {jay.name} library.Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Add a Book")
        user_choice =int(input())

        if user_choice==1:

            jay.displayBooks()
            

        elif user_choice ==2:
            book=input("Enter the name of the book you want to lend:")
            name=input("Enter your name")
            jay.lendBook(user,book)

        elif user_choice ==3:
            book=input("Enter the name of the book you want to add:")
            jay.addBook(book)
        elif user_choice ==4:
            book=input("Enter the name of the book you want to return:")
            jay.returnBook(book)
        else:
            print("Not a valid option")
            print("Press q to quit and c to continue")
    user_choice2=" "
    while(user_choice!="c" and user_choice!="q"):
        user_choice2 = input()
        if user_choice2 == 'q':
            exit()
        if user_choice2 == 'c': 
            continue