from classes.room import Room
from classes.book import Book
from rich.table import Table
from rich.console import Console
from rich.text import Text
import readchar
from readchar import key
from typing import List
from os import system, name
from rich import print

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
        print(self.return_hexagon())
        # while True:
        #     self.clear_console()

        #     # print output handles all of the output in a singular screen, to center it
        #     print_output = "Press enter to lock in the room number\n"

        #     # Printing the number input
        #     print_output += "← Room number: "
        #     for i in range(len(number_list)):
        #         if i == current_edited_index:
        #             print_output += "[u]" + str(number_list[i]) + "[/u] "
        #         else:
        #             print_output += str(number_list[i]) + " "
        #     print_output += " →\n"
        #     # ----------


        #     # Print the hexagon

            
        #     # wpisywanie znaku powinno być na samym końcu !!!!!! top 10 okrętów
        #     k = readchar.readkey()
        #     if k == key.LEFT:
        #         self.decrement_list(number_list)
        #     elif k == key.RIGHT:
        #         self.increment_list(number_list)
        #     elif k == key.ENTER:
        #         break
        #     elif k in ('0','1','2','3','4','5','6','7','8','9'):
        #         if current_edited_index >= 8:
        #             current_edited_index = 0
        #         number_list[current_edited_index] = int(k)
        #         current_edited_index += 1

                    
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

    def increment_list(self, list_of_numbers: List[int]):
            for i in range(len(list_of_numbers) - 1, -1, -1):
                if list_of_numbers[i] == 9:
                    list_of_numbers[i] = 0
                else:
                    list_of_numbers[i] += 1
                    return
            list_of_numbers.insert(0,1)
            return
    
    def decrement_list(self, list_of_numbers: List[int]):
        for i in range(len(list_of_numbers) - 1, -1, -1):
            if list_of_numbers[i] == 0:
                if(list_of_numbers[i - 1] != 0):
                    list_of_numbers[i - 1] -= 1
                    list_of_numbers[i] = 9
            else:
                list_of_numbers[i] -= 1
                return
        return
            
    def clear_console(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    #          ██████████          
    #        ██          ██
    #      ██              ██
    #    ██                  ██
    #  ██                      ██
    #██                          ██
    #  ██                      ██
    #    ██                  ██
    #      ██              ██
    #        ██          ██
    #          ██████████
    def return_hexagon(self, size: int = 5):
        hexagon_string = ""
        for i in range(size):
            hexagon_string += "  "
        for i in range(size):
            hexagon_string += "██"
        hexagon_string += "\n"

        for i in range(size):
            for j in range(size):
                hexagon_string += " "
            hexagon_string += "██"
        return hexagon_string


