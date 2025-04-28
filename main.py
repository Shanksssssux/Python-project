from fastapi import FastAPI

app = FastAPI()

books = []
book_id = 1

@app.post("/books")
def Add_Books(title:str, author: str, year: int):
    global book_id
    Book1={
        "id":book_id,"title": title,"author":author,"year":year
    }
    book_id += 1
    books.append(Book1)
    return Book1

@app.get("/books")
def get_books():
    return books

@app.delete("/books/book_id")
def Delete_Books(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}

@app.get("/books/book_id")
def View_Book_By_ID(book_id : int):
    for book in books:
        if book["id"] == book_id:
            return book

@app.get("/books/title")
def View_Book_By_Title(title : str):
    for book in books:
        if book["title"] == title:
            return book

@app.put("/books/book_id")
def Update_Book_By_ID(book_id : int, title:str, author:str, year:int):
    for book in books:
        if book["id"] == book_id:
            if title:
                book["title"] = title
            if author:
                book["author"] = author
            if year:
                book["year"] = year
            return book

