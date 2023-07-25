# Project 3 - Student Library System

# Explanation - Implement a student library system using OOPs
# where students can borrow a book from the list of books.
# Create a separate library and student class. Your program must be menu driven. You are free to choose methods and attributes of your choice to implement the functionality.


class library:

    def __init__(self):
        self.books = ["Algorithm", "Django", "Python", "Java", "C++", "Php", "Node.Js", "HTML"]
        self.dup = ["Algorithm", "Django", "Python", "Java", "C++", "Php", "Node.Js", "HTML"]
        self.b = ["algorithm", "django", "python", "java", "c++", "php", "node.js", "html"]


    def show_books(self):
        print("===== Books available in the Library =====")
        for i in self.books:
            print("      * " +i)
        print("\n")


class student(library):
    
    def borrow_books(self):
        self.name = input("Enter name of the book: - ")
        

        if self.name.lower() in self.b:
            student_name = input("Enter recipient's name: ")
            self.books.remove(self.books[self.b.index(self.name.lower())])
            print(f"{self.books[self.b.index(self.name.lower())]} book has been claimed by {student_name}.\n")
        else:
            print(f"{self.name} book is not available.\n")

    
    def return_book(self):
        self.sender_name = input("Enter your name: ")
        self.book_name = input("Enter book's name: ")

        for j in self.b:
            if j != self.book_name.lower():
                pass
            else:
                self.library.books.append(self.dup[self.b.index(self.book_name.lower())])
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


# class Library:
#     def __init__(self):
#         self.books = ["Algorithm", "Django", "Python", "Java", "C++", "Php", "Node.Js", "HTML"]

#     def show_books(self):
#         print("===== Books available in the Library =====")
#         for i in self.books:
#             print("      * " + i)


# class Student:
#     def __init__(self, library):
#         self.library = library
#         self.borrowed_books = []

#     def borrow_book(self, student_name, book_name):
#         book_name_lower = book_name.lower()
#         if book_name_lower in self.borrowed_books:
#             print(f"You have already borrowed {book_name}.")
#         elif book_name in self.library.books:
#             self.borrowed_books.append(book_name_lower)
#             self.library.books.remove(book_name)
#             print(f"{student_name} borrowed {book_name} book.")
#         else:
#             print(f"{book_name} book is not available in the library.")

#     def return_book(self, student_name, book_name):  # Include student's name as an argument
#         book_name_lower = book_name.lower()
#         if book_name_lower in self.borrowed_books:
#             self.borrowed_books.remove(book_name_lower)
#             self.library.books.append(book_name)
#             print(f"{student_name} returned {book_name} book.")  # Include student's name
#         else:
#             print(f"You have not borrowed {book_name} book.")


# def show_menu():
#     print("========== Enter any choice ==========")
#     print("1. Books in the Library")
#     print("2. Request a book")
#     print("3. Return a book")
#     print("4. Exit Library")
#     return int(input("Enter: "))


# def main():
#     library = Library()
#     student = Student(library)

#     while True:
#         choice = show_menu()

#         if choice == 1:
#             library.show_books()
#         elif choice == 2:
#             book_name = input("Enter the name of the book: ")
#             student_name = input("Enter your name: ")
#             student.borrow_book(student_name, book_name)
#         elif choice == 3:
#             book_name = input("Enter the name of the book: ")
#             student_name = input("Enter your name: ")
#             student.return_book(student_name, book_name)  # Pass student's name as an argument
#         elif choice == 4:
#             print("Exiting Library. Goodbye!")
#             break
#         else:
#             print("Invalid Choice!!")


# if __name__ == "__main__":
#     main()
