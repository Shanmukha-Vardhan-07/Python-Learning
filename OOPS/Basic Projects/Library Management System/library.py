class Book:
    def __init__(self,book_id,title,author,genre,total_copies):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.genre=genre
        self.total_copies=total_copies
        self.available_copies=total_copies

    def is_available(self):
        return self.available_copies > 0
    
    def __str__(self):
        return (
            f"Book Id:{self.book_id}"
            f"Title: {self.title}"
            f"Author: {self.author}"
            f"Genre: {self.genre}"
            f"Available: {self.available_copies}/{self.total_copies}"
        )

class Member:
    MAX_Books=3
    def __init__(self,member_id,name,email):
        self.member_id=member_id
        self.name=name
        self.email=email
        self.borrowed_books=[]

    def borrow_book(self,book):
        if book in self.borrowed_books:
            raise ValueError(f"{self.name} is already borrowed ")
        if len(self.borrowed_books) >= Member.MAX_Books:
            raise ValueError(f"{self.name} has already borrowed more then 3 books")
        if not book.is_available():
            raise ValueError(f"{book.title} is not available")
        
        self.borrowed_books.append(book)
        book.available_copies-=1

        print(f"{self.name} borrowed {book.title} successfully")

    def return_book(self,book):
        if book not in self.borrowed_books:
            raise ValueError(f"{self.name} never borrowed {book.title}")
        
        self.borrowed_books.remove(book)
        book.available_copies+=1

        print(f"{self.name} returned {book.title} successfully")

    def view_borrowed(self):
        if not self.borrowed_books:
            print(f"{self.name} has not borrowed any books")
            return
        
        print(f"Books Borrowed by {self.name}")
        for book in self.borrowed_books:
            print(book)

    def __str__(self):
        return (
            f"Member ID: {self.member_id} | "
            f"Name: {self.name} | "
            f"Email: {self.email}"
            )

class Library:
    def __init__(self,name):
        self.name=name
        self.books={}
        self.members={}

    def add_book(self,book):
        self.books[book.book_id]=book
        print(f"Book {book.title} added to library")

    def register_member(self,member):
        self.members[member.member_id]=member
        print(f"Member {member.name} registered successfully")

    def issue_book(self,member_id,book_id):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")
        
        member=self.members[member_id]
        book=self.books[book_id]

        member.borrow_book(book)

    def return_book(self,member_id,book_id):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")
        
        member=self.members[member_id]
        book=self.books[book_id]

        member.return_book(book)

    def search_by_title(self,title):
        results=[]

        for book in self.books.values():
            if title.lower() in book.title.lower():
                results.append(book)

        return results
    
    def search_by_author(self,author):
        results=[]

        for book in self.books.values():
            if author.lower() in book.author.lower():
                results.append(book)

        return results
    
    def show_available_books(self):
        print(f"Available Book in {self.name}")
        found=False

        for book in self.books.values():
            if book.available_copies > 0:
                print(book)
                found=True

        if not found:
            print("No books Available")

    def member_report(self,member_id):
        if member_id not in self.members:
            raise ValueError("Member not found")

        member = self.members[member_id]

        print(f"\nMember Report for {member.name}")
        print("-" * 40)

        if not member.borrowed_books:
            print("No books borrowed")
        else:
            for book in member.borrowed_books:
                print(book)

library = Library("City Library")

book1 = Book("B001", "Clean Code", "Robert Martin", "Tech", 3)
book2 = Book("B002", "Python Crash Course", "Eric Matthes", "Programming", 2)
book3 = Book("B003", "Atomic Habits", "James Clear", "Self Help", 1)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

member1 = Member("M001", "Shanmukh", "s@email.com")

library.register_member(member1)

library.show_available_books()

library.issue_book("M001", "B001")
library.issue_book("M001", "B002")


library.member_report("M001")

library.return_book("M001", "B001")

member1.view_borrowed()

print("\nSearch by Title:")
results = library.search_by_title("Python")

for book in results:
    print(book)

print("\nSearch by Author:")
results = library.search_by_author("James")

for book in results:
    print(book)
