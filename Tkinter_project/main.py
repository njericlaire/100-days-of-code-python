
from tkinter import *
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)


equal= Label(text="is equal to")
equal.grid(row=1,column=0)


miles = Label(text="Miles")
miles.grid(row=0,column=3)

km= Label(text="km")
km.grid(row=1,column=3)

answer= Label(text="0")
answer.grid(row=1,column=2)

def calculate():
    mile=float(entry.get())
    kilo=mile*1.6
    answer.config(text=f"{kilo}")

button = Button(text="Calculate", command=calculate)
button.grid(row=2,column=2)

entry = Entry(width=30)
entry.insert(END, string="0")
entry.grid(row=0,column=2)


window.mainloop()
