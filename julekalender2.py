from tkinter import *
import tkinter.font as tkFont
import datetime

root = Tk()

overskrift = tkFont.Font(family="Helvetica")
root.title("Julekalender")

overskrift = Label(root, text="Julekalender 2024", width=80, height=6, font=overskrift)
overskrift.configure(fg="white", bg="red")
overskrift.grid(row=0, column=0, padx=100, pady=20, columnspan=6)

root.configure(background="darkred")
root.minsize(900, 500)
root.maxsize(900, 500)


# Kode laget av AI for å hjelpe meg med å passe på at alle knappene er på riktig plass 

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

# Koden for å lage 24 knapper

knapper = []
for i in range(1, 25):
    knapp = Button(root, text=str(i), width=10, height=3, font=("Helvetica", 12), fg="white", bg="darkgreen")
    row = (i - 1) // 6 + 1
    col = (i - 1) % 6
    knapp.grid(row=row, column=col, padx=10, pady=10)
    knapper.append(knapp)

root.mainloop()
