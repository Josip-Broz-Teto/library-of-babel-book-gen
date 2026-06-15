import random
import linecache
import math

class Book:
    # this is every possible combination of signs in a book
    allPossibleCombinations = 29**120000

    # fields defining the position of the book
    book_id : int
    book_title : str = ""

    def __init__(self, seed: int, room_id: str, wall_number: int, shelf_number: int, volume_number: int):
        if room_id < 1 or room_id > 99999999 :
            print("not 8 letters")
            return
        if wall_number > 4 or wall_number < 1 :
            print("wallNumber bigger than 4, smaller than 1")
            return

        if shelf_number > 8 or shelf_number < 1 :
            print("shelfNumber bigger than 8, smaller than 1")
            return

        if volume_number > 16 or volume_number < 1 :
            print("volumeNumber bigger than 16, smaller than 1")
            return

        # book id is unique in the whole library
        self.book_id = (
            (self.seed * 10) +
            (self.room_id * 1000) +
            (self.wall_number * 100000) +
            (self.shelf_number * 10000000) +
            (self.volume_number * 100000000)
        )

        # here the name of the book is determined
        random.seed(self.book_id)
        ran_num = random.randint(1,5)

        lenght_of_title = ran_num
        if lenght_of_title == 0:
            lenght_of_title = 1
        
        while lenght_of_title != 0:
            ran_num = random.randint(1, 10001)
            new_line = linecache.getline("words.txt", ran_num)
            self.book_title += new_line.strip() + " "
            lenght_of_title -= 1

    # converts a number to letters
    def convert_to_text(number: int):
        letters = "qwertyuiopasdfghjklzxcvbnmw,."
        content = ""

        while number > 0:
            content += letters[number % 29]
            number = math.floor(number / 29)
            
        return content
    
    # given a page between 1 and 100, get text unique to it
    def get_page(self, page_number: int) -> str:
        if self.room_id == None:
            print("set stats first")

        random.seed(self.book_id + page_number)
        # this big number guarantees that it always fills a page
        page_content_int = random.randint(29**1199, (29**1200) - 1)
        page_content_int_string = str(page_content_int)
        page_content_converted = ""

        for i in range(0, len(page_content_int_string), 5):
            chunk = page_content_int_string[i:i+5]
            page_content_converted += self.convert_to_text(int(chunk))
    
        return page_content_converted
            
    