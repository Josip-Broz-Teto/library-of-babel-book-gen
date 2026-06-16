from classes.room import Room
from classes.book import Book
from rich.table import Table
from rich.console import Console
from rich.text import Text
import readchar
from readchar import key
from typing import List

class Ui:
    seed : int
    current_room : Room
    current_selection : str = "room"
    current_displayed_book : Book

    # pixels and other goodies for rich printing
    console : Console = Console()

    pixel = Text("██", style="white")

    def __init__(self, seed):
        self.seed = seed
        self.current_room = Room(seed, 0)
        self.current_displayed_book = Book(seed, 0, 1, 1, 1)

    def show_room_ui(self):
        print("press enter to lock in a room")
        current_edited_index = 0
        number_list = [0,0,0,0,0,0,0,0]
        while True:
            print("← Room number: " + str(number_list) + " →")
            k = readchar.readkey()
            if k == key.LEFT:
                self.decrement_list(number_list)
            elif k == key.RIGHT:
                self.increment_list(number_list)
            elif k == key.ENTER:
                break
            elif k in ('0','1','2','3','4','5','6','7','8','9'):
                if current_edited_index >= 8:
                    current_edited_index = 0
                number_list[current_edited_index] = int(k)
                current_edited_index += 1
                    
        # reszta

    def show_wall_ui(self):
        print("choose a wall (between 1 and 4)")
        new_wall_number = input("")
        self.current_room.change_wall(new_wall_number)

    def show_shelf_ui(self):
        print("choose a shelf (between 1 and 8)")
        new_shelf_number = input("")
        self.current_room.change_shelf(new_shelf_number)

    def show_volume_ui(self):
        print("choose a volume (between 1 and 16)")
        new_volume_number = input("")
        self.current_displayed_book = self.current_room.get_book(new_volume_number, self.seed)

    def display_book_pages(self):
        print("page 1 of " + str(self.current_displayed_book.get_page(14)))
        print("")
        print(self.current_displayed_book.get_page(self.current_displayed_book.current_page))

    def increment_list(self, list_of_numbers: List[int], max_size : int = 8):
            for i in reversed(list_of_numbers):
                if list_of_numbers[i] == 9:
                    list_of_numbers[i] = 0
                    pass
                else:
                    list_of_numbers[i] += 1
                    return
            list_of_numbers.append(1)
            return
    
    def decrement_list(self, list_of_numbers: List[int], max_size : int = 8):
        for i in reversed(list_of_numbers):
            if list_of_numbers[i] == 0:
                list_of_numbers[i - 1] = 9
                pass
            else:
                list_of_numbers[i] -= 1
                return
        list_of_numbers.append(1)
        return

