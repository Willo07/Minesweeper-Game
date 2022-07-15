from tkinter import *
from cell import Cell
import settings
import utilities


root = Tk()
# Override the settings of the Window
root.config(bg="black")
root.geometry(f'{settings.width}x{settings.height}')
root.title("Mine SeeKer")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.width,
    height=utilities.height_prct(25)
)
top_frame.place(
    x=0,
    y=0
)

left_frame = Frame(
    root,
    bg='black',
    width=utilities.width_prct(25),
    height=utilities.height_prct(75)
)
left_frame.place(
    x=0,
    y=utilities.height_prct(25)
)

center_frame = Frame(
    root,
    bg='black',
    width=utilities.width_prct(75),
    height=utilities.height_prct(75)
)
center_frame.place(
    x=utilities.width_prct(25),
    y=utilities.height_prct(25)
)

for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# Call the Label from Cell Class
Cell.create_cell_count_label(left_frame)
Cell.Cell_count_label_obj.place(x=0, y=0)
Cell.randomize_mines()


# Run the window
root.mainloop()
