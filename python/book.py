
from typing import List


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def list_print(self) -> None:
        print("\n現在の在庫\n")
        for book in self.books:
            print("="*20)
            print(f"タイトル: {book.title}\n 著者: {book.author}\n ISBN: {book.isbn}\n 出版年: {book.year}\n 価格: {book.price}\n 在庫: {book.quantity}")
            print("="*20)

    def register(self, title: str, author: str, isbn: int, year: int,price: int,quantity: int = 1):
        exist = False
        for book in self.books:
            if book.isbn == isbn:
                exist = True
                book.quantity += quantity
        if exist==False:
            new_book = Book(title,author,isbn,year,price,quantity)
            self.books.append(new_book)

    def update(self):
        pass
        
        
class Book:
    def __init__(self, title: str, author: str, isbn: int, year: int, price: int, quantity: int=1) -> None:
        self.title = title 
        self.author = author 
        self.isbn = isbn 
        self.year = year
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":

    library_A = Library()

    library_A.register("Python入門","柳沼 裕太",12345678,2014,1980,3)
    
    library_A.list_print()

    library_A.register("Python入門","柳沼 裕太",12345678,2014,1980,2)
    
    library_A.register("Java入門","田中 太郎",12342525,2012,3980,7)    

    library_A.list_print()
        