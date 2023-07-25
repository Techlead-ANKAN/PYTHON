# Project 3 - Student Library System

# Explanation - Implement a student library system using OOPs
# where students can borrow a book from the list of books.
# Create a separate library and student class. Your program must be menu driven. You are free to choose methods and attributes of your choice to implement the functionality.


class library:

    def __init__(self):
        self.books = ["Algorithm", "Django", "Python", "Java", "C++", "Php", "Node.Js", "HTML"]
        self.dup = ["Algorithm", "Django", "Python", "Java", "C++", "Php", "Node.Js", "HTML"]  # DUPLICATE
        self.b = ["algorithm", "django", "python", "java", "c++", "php", "node.js", "html"]   # lower


    def show_books(self):
        print("===== Books available in the Library =====")
        for i in self.books:
            print("      * " +i)
        print("\n")


class student(library):
    
    def borrow_books(self):
        print("\n")
        self.name = input("Enter name of the book: - ")
        

        if self.name.lower() in self.b:
            student_name = input("Enter recipient's name: ")
            self.books.remove(self.books[self.b.index(self.name.lower())])
            print(f"{self.dup[self.b.index(self.name.lower())]} book has been claimed by {student_name}. Return the book within 30 days.\n")
        else:
            print(f"{self.name} book is not available.\n")

    
    def return_book(self):
        print("\n")
        self.sender_name = input("Enter your name: ")
        self.book_name = input("Enter book's name: ")

        for j in self.b:
            if j != self.book_name.lower():
                pass
            else:
                self.books.append(self.dup[self.b.index(self.book_name.lower())])
                print(f"{self.dup[self.b.index(self.book_name.lower())]} has been returned.\n")
                break





S1 = student()
# print(S1.show_books())

while (True):
    print("========== Enter any choice ==========")
    print("1. Books in the Library")
    print("2. Request a book")
    print("3. Add/Return books")
    print("4. Exit Library")
    ch = int(input("Enter: "))



    if ch == 1:
        S1.show_books()
    elif ch == 2:
        S1.borrow_books()
    elif ch == 3:
        S1.return_book()
    elif ch == 4:
        exit()
    else:
        print("Invalid Choice!!")

