#BOOK_.PY FIrst portion
import add_books
import view_all_books
all_books =[]
while True:
    print("Welcome to library mangement system")
    print("0.Exit")
    print("1.Add books")
    print("2.View all books")
    menu=input("Select any numbers:")
    if menu=="0":
        print("THanks for using library mangement system")
        break
    elif menu=="1":
        all_books=add_books.add_books(all_books)
    elif menu=="2":
        view_all_books.view_all_books(all_books)
    else:
        print("choose a valid number")
 

 #Add books portion
from save_all_books import save_all_books
def add_books(all_books):
    title=input("enter book title:")
    author=input("enter author name:")
    isbn=int(input("enter the isbn number:"))
    year=int(input("enter the year name:"))
    price=int(input("enter the price:"))
    quantity=int(input("enter the quantity:"))
    book={
        "title":title,
        "author":author,
        "isbn":isbn,
        "year":year,
        "price":price,
        "quantity":quantity,
    }
    all_books.append(book)
    save_all_books(all_books)
    print("books added successfully")
    return all_books 


 #save all books portion
def save_all_books(all_books):
    with open("all_books.csv","w") as fp:
        for book in all_books:
            line=f"{book['title']},{book['author']},{book['isbn']},{book['year']},{book['price']},{book['quantity']}\n"
            fp.write(line)


 #view all books portion

def view_all_books(all_books):
    if all_books != []:
        for book in all_books:
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']}")
    else:
        print("No Book found in program")

