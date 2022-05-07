from tkinter import *
from cell import Cell
import settings
import utils

# Configuraciones de la ventana
root = Tk()
root.configure(bg="#000")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

# Frames
topFrame = Frame(root, bg='#000', width=settings.WIDTH, height=utils.heightPrct(25))
topFrame.place(x=0, y=0)
leftFrame = Frame(root, bg='#000', width=utils.widthPrct(25), height=utils.heightPrct(75))
leftFrame.place(x=0, y=utils.heightPrct(25))
centerFrame = Frame(root, bg='#ccc', width=utils.widthPrct(75), height=utils.heightPrct(75))
centerFrame.place(x=utils.widthPrct(25), y=utils.heightPrct(25))

# Titulo del juego en pantalla
gameTitle = Label(topFrame, bg='black', fg='white', text='Buscaminas Equisdé', font=('', 48))
gameTitle.place(x=utils.widthPrct(28), y=utils.heightPrct(5))

# Mostrar las celdas en pantalla
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.createBtnObject(centerFrame)
        c.cellBtnObject.grid(column=x, row=y)

# Llamar la etiqueta que muestra las celdas restantes de la clase Cell
Cell.createCellCountLabel(leftFrame)
Cell.cellCountLabelObject.place(x=0, y=0)

Cell.randomizeMines()

# Ejecuta la ventana
root.mainloop()
