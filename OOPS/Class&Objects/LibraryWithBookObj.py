class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)
        print(f"{book.title} is added succesfully")

    def remove_book(self,title):
        for book in self.books:
            if book.title.lower()==title.lower():
                self.books.remove(book)
                print(f"{title} is removed succesfully")
                return
            print("Book not found")

    def search_by_author(self,author):
        found=False

        print(f"Books by {author}")

        for book in self.books:
            if book.author.lower()==author.lower():
                print("-",book.title)
                found=True

            if not found:
                print("No books found")

library=Library()

while True:
    print("---- Library Menu----")
    print("1.Add Book")
    print("2.Remove Book")
    print("3.search book by author name")
    print("Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        title=input("Enter the book title:")
        author=input("Enter the author name:")

        book=Book(title,author)

        library.add_book(book)

    elif choice==2:
        title=input("Enter the title to remove:")

        library.remove_book(title)

    elif choice==3:
        author=input("Enter the author name to search:")

        library.search_by_author(author)

    elif choice==4:
        print("Exiting Library system")
        break
    else:
        print("Invalid choice")            

