# Import dependencies
import pandas as pd
import numpy as np

class BookLover():

    acceptable_ratings = range(6)

    def __init__(self, name: str, email: str, fav_genre: str, num_books : int = 0, book_list: pd.DataFrame = pd.DataFrame({'book_name':[], 'book_rating': []})) -> None:
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name: str, rating: int) -> None:
        if rating not in self.acceptable_ratings:
            raise ValueError("Not an acceptable rating value.")
        
        if book_name in self.book_list['book_name'].tolist():
            print("That book already exists in the list")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books = len(self.book_list)

    def has_read(self, book_name: str) -> bool:
        return book_name in self.book_list['book_name'].tolist()
    
    def num_books_read(self) -> int:
        return self.num_books
    
    def fav_books(self) -> pd.DataFrame:
        return self.book_list.loc[(self.book_list['book_rating'] > 3)]
    

if __name__ == '__main__':

    test_object = BookLover("Han Solo", "hsolo@milleniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)

    print(f"Has read 'War of the Worlds': {test_object.has_read("War of the Worlds")}")
    print(f"Has read 'Harry Potter': {test_object.has_read("Harry Potter")}")
    print(f"Number of books read: {test_object.num_books}")
    print(test_object.fav_books())
