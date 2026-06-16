from classes.ui import Ui

# seed for this world (funny 67)
seed = 2137**67

ui = Ui(seed)

ui.show_room_ui()
ui.show_wall_ui()
ui.show_shelf_ui()
ui.show_volume_ui()
ui.display_book_pages()