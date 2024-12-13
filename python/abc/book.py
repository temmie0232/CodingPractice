
from typing import List, Optional

class Book:
    def __init__(self, title: str, author: str, isbn: int, year: int, price: int, quantity: int=1) -> None:
        self.title = title 
        self.author = author 
        self.isbn = isbn 
        self.year = year
        self.price = price
        self.quantity = quantity


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []     # 本を格納

    # すべての本を出力
    def books_print(self) -> None:
        print("\n現在の在庫\n")
        if self.books:
            for book in self.books:
                print("="*20)
                print(f"タイトル: {book.title}\n 著者: {book.author}\n ISBN: {book.isbn}\n 出版年: {book.year}\n 価格: {book.price}\n 在庫: {book.quantity}")
                print("="*20)
        else:
            print("本が登録されていません")
    
    # 受け取った本を出力
    def book_print(self, book: Book) -> None:
        if book:
            print("\n現在の在庫\n")
            print("="*20)
            print(f"タイトル: {book.title}\n 著者: {book.author}\n ISBN: {book.isbn}\n 出版年: {book.year}\n 価格: {book.price}\n 在庫: {book.quantity}")
            print("="*20)
        else:
            print("その本は存在しません")

    # タイトルから本を探し返す
    def get_book_by_title(self, title: str) -> Optional[Book]:
        for book in self.books:
            if book.title == title:
                return book
        return None

    # isbnから本を探し返す
    def get_book_by_isbn(self, isbn: int) -> Optional[Book]:
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    # 新しい本の登録
    def register(self, title: str, author: str, isbn: int, year: int, price: int, quantity: int = 1) -> None:
        exist = False
        for book in self.books:
            # 本が既に存在する場合は在庫を増やす
            if book.isbn == isbn:
                exist = True
                book.quantity += quantity
        # 存在しない場合リストに追加(登録)
        if not exist:
            new_book = Book(title,author,isbn,year,price,quantity)
            self.books.append(new_book)

    # 本の削除
    def delete(self, isbn: int, quantity: int) -> None:
        exist = False
        for book in self.books:
            if book.isbn == isbn:
                exist = True
                book.quantity -= quantity
        if not exist:
            print("その本は存在しません")

    # isbnと更新値を受け取り、値を更新
    def update(self,isbn,**kwargs) -> None:
        # isbnから本を受け取る
        book = self.get_book_by_isbn(isbn)
        # itemsでkwargs(辞書)からキーとバリューを取得
        for key,value in kwargs.items():
            # key属性が存在するなら
            if hasattr(book,key):
                # その本のkeyにvalueを適用
                setattr(book,key,value)


if __name__ == "__main__":

    library_A = Library()

    library_A.register("Python入門","柳沼 裕太",12345678,2014,1980,3)
    