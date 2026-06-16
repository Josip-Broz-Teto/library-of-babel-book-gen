from classes.book import Book

class Room:
    room_id : int = 0
    current_wall_number : int = 0
    current_shelf_number : int = 0
    seed : int = 1

    def __init__(self,  seed: int, room_id: int):
        self.room_id = room_id
        self.seed = seed

    def change_wall(self, new_wall_number : int):
        self.current_wall_number = new_wall_number

    def change_shelf(self, new_shelf_number : int):
        self.current_shelf_number = new_shelf_number

    def get_book(self, volume_number: int) -> Book:
        return Book(self.seed, self.room_id, self.current_wall_number, self.current_shelf_number, volume_number)