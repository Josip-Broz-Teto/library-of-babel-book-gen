from classes.room import Room
from classes.book import Book

class Ui:
    current_room : Room
    current_selection : str = "room"
    current_displayed_book : Book
    seed : int

    def __init__(self, seed):
        self.seed = seed

    def show_room_ui(self):
        print("choose a room (8 numbers)")
        new_room_id = input("")
        self.current_room = Room(self.seed, new_room_id)

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
        print("page 1 of " + self.current_displayed_book.get_page)
        print("")
        print(self.current_displayed_book.get_page(self.current_displayed_book.current_page))