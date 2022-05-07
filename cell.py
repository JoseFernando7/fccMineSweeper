from tkinter import Button, Label, messagebox
import random
import settings
import sys


class Cell:
    all = []
    cellCountLabelObject = None
    cellCount = settings.CELL_COUNT

    def __init__(self, x, y, isMine=False):
        self.isMine = isMine
        self.isMineCandidate = False
        self.isOpened = False
        self.cellBtnObject = None
        self.x = x
        self.y = y

        # Añadir el objeto a la lista Cell.all
        Cell.all.append(self)

    def createBtnObject(self, location):
        btn = Button(location, width=12, height=4)
        btn.bind('<Button-1>', self.leftClickActions)
        btn.bind('<Button-3>', self.rightClickActions)
        self.cellBtnObject = btn

    @staticmethod
    def createCellCountLabel(location):
        lbl = Label(location, bg='black', fg='white', text=f"Quedan {settings.CELL_COUNT - 9} celdas", width=20, height=4,
                    font=("", 20))
        Cell.cellCountLabelObject = lbl

    def leftClickActions(self, event):
        if self.isMine:
            self.showMine()
        else:
            if self.surroundedCellsMinesLength == 0:
                for cellObj in self.surroundedCells():
                    cellObj.showCell()
            self.showCell()
            # self.cellBtnObject.configure(state='disabled', fg='black')

            # Si el numeros de minas es igual al numero de celdas que quedan, el jugador gana
            if Cell.cellCount == settings.MINES_COUNT:
                messagebox.showinfo('You win', 'No quedan minas, has ganado')
        self.cellBtnObject.unbind('<Button-1>')
        self.cellBtnObject.unbind('<Button-3>')

    def rightClickActions(self, event):
        if not self.isMineCandidate:
            self.cellBtnObject.configure(bg='orange', activebackground='orange')
            self.isMineCandidate = True
        else:
            self.cellBtnObject.configure(bg='#d9d9d9', activebackground='#f0f0f0')
            self.isMineCandidate = False

    def showMine(self):
        # Una logica que interrumpe el juego y muestra un mensaje de que el jugador perdio
        self.cellBtnObject.configure(bg='red', activebackground='red')
        messagebox.showerror("Game Over", "Has caído en una mina, F")
        sys.exit()

    def surroundedCells(self):
        cells = [
            self.getCellByAxis(self.x - 1, self.y - 1),
            self.getCellByAxis(self.x - 1, self.y),
            self.getCellByAxis(self.x - 1, self.y + 1),
            self.getCellByAxis(self.x, self.y - 1),
            self.getCellByAxis(self.x + 1, self.y - 1),
            self.getCellByAxis(self.x + 1, self.y),
            self.getCellByAxis(self.x + 1, self.y + 1),
            self.getCellByAxis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surroundedCellsMinesLength(self):
        counter = 0
        for cell in self.surroundedCells():
            if cell.isMine:
                counter += 1

        return counter

    def showCell(self):
        if not self.isOpened:
            Cell.cellCount -= 1
            self.cellBtnObject.configure(text=self.surroundedCellsMinesLength)
            # Reemplaza el texto de el contador de celdas con la nueva cuenta
            if Cell.cellCountLabelObject:
                Cell.cellCountLabelObject.configure(text=f"Quedan {Cell.cellCount - 9} celdas")
                # Si esta celda fue mineCandidate, se cambia al color por defecto si se clicka
                self.cellBtnObject.configure(bg='#d9d9d9', activebackground='#f0f0f0')

        # Marca la casilla como abierta (Se usa como la ultima linea de este metodo)
        self.isOpened = True

    def getCellByAxis(self, x, y):
        # Retorna una celda objeto basado en el valor de x, y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @staticmethod
    def randomizeMines():
        pickedCells = random.sample(Cell.all, settings.MINES_COUNT)
        for pickedCells in pickedCells:
            pickedCells.isMine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'
