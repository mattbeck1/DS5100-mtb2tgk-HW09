import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Matt", "mtb2tgk@virginia.edu", "fantasy")
        test_object.add_book("Harry Potter", 4)
        self.assertTrue("Harry Potter" in test_object.book_list['book_name'].tolist())

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Matt", "mtb2tgk@virginia.edu", "fantasy")
        test_object.add_book("Harry Potter", 4)
        test_object.add_book("Harry Potter", 4)

        actual = test_object.book_list['book_name'].value_counts()['Harry Potter']
        expected = 1

        self.assertEqual(actual, expected)


    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Matt", "mtb2tgk@virginia.edu", "fantasy")
        test_object.add_book("Harry Potter", 4)

        self.assertTrue(test_object.has_read("Harry Potter"))

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Matt", "mtb2tgk@virginia.edu", "fantasy")
        test_object.add_book("Harry Potter", 4)

        self.assertFalse(test_object.has_read("War of the Worlds"))

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Matt", "mtb2tgk@virginia.edu", "fantasy")
        test_object.add_book("Harry Potter I", 4)
        test_object.add_book("Harry Potter II", 2)
        test_object.add_book("Harry Potter III", 3)
        test_object.add_book("Harry Potter IV", 1)
        test_object.add_book("Harry Potter V", 5)
        test_object.add_book("Harry Potter VI", 0)
        test_object.add_book("Harry Potter VII", 4)

        actual = test_object.num_books_read()
        expected = 7

        self.assertEqual(actual, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object = BookLover("Matt", "mtb2tgk@virginia.edu", "fantasy")
        test_object.add_book("Harry Potter I", 4)
        test_object.add_book("Harry Potter II", 2)
        test_object.add_book("Harry Potter III", 3)
        test_object.add_book("Harry Potter IV", 1)
        test_object.add_book("Harry Potter V", 5)
        test_object.add_book("Harry Potter VI", 0)
        test_object.add_book("Harry Potter VII", 4)

        actual = all([x > 3 for x in test_object.fav_books()['book_rating'].tolist()])

        self.assertTrue(actual)


if __name__ == '__main__':
    
    unittest.main(verbosity=3)