import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQL.Installer",
    database = "library_management"
)
print("Connected successfully")

mycursor = mydb.cursor()
mycursor.execute("""
    CREATE TABLE Books(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        ISBN VARCHAR(255)
    )
""")
print("Table created successfully")

mycursor.execute("DESCRIBE Books")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

def add_book():
    while True:
        title = input("Enter title: ")
        author = input("Enter name(s) of the author: ")
        ISBN = input("Enter the ISBN of the book: ")
    
        sql = "INSERT INTO Books (title, author, ISBN) VALUES(%s, %s, %s)"
        val = (title, author, ISBN)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "book(s) inserted")
        response = input("Do you want to add another book? (YES/NO): ").strip().lower()
        if response == "no":
            print("Thanks for the adds today. See you next time!")
            break
        elif response != "yes":
            print("Unrecognized input. Exiting!")
            break
add_book()

def search_for_books():
    res = input("Enter the title your searching: ").strip()
    sql = "SELECT title, author, ISBN FROM Books WHERE title = %s"
    val = (res,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if myresult:
        for book in myresult:
             print("Title:",book[0], "Author:",book[1], "ISBN:",book[2])
    else:
        print("Book not found in the library")
search_for_books()

def list_books():
    sql = "SELECT * FROM Books" 
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if myresult:
        print(f"{"ID":<5} {"Title":<25} {"Author":<20} {"ISBN":<15}")
        print("-" * 70)

        for info in myresult:
            print(f"{info[0]:<5} {info[1]:<25} {info[2]:<20} {info[3]:<15}")
    else:
        print("No books found in our library")
list_books()

def delete_book():
    num = input("Enter id to delete: ")
    sql = "SELECT id FROM books WHERE id = %s"
    val = (num,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if myresult:
        sql = "DELETE FROM Books WHERE id = %s"
        val = (num,)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Book deleted successfully")
    else:
        print("Input id not found")
delete_book()