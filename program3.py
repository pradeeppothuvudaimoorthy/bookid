books = {
    101: "Python Programming",
    102: "Data Structures",
    103: "Operating System",
    104: "Computer Networks",
    105: "Database Management System"
}


book_id = int(input("Enter Book ID to search: "))

if book_id in books:
    print("Book Found!")
    print("Book ID:", book_id)
    print("Book Name:", books[book_id])
else:
    print("Book not found.")