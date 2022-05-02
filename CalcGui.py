from tkinter import *

window = Tk()
window.title("계산기")

num = [['7','8','9','/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['c', '0', '.', '+']]

input = Entry(window, width=40)
input.grid(column=0, row=0, columnspan=4)
output = Label(window, text="", width=20)
output.grid(column=2, row=1, columnspan=3)

def numButton(num):
    if num == 'c':
        input.delete(0, END)
    else:
        input.insert(END, num)

def calc():
    output.config(text=eval(input.get()))

for i in range(4):
    for j in range(4):
        button = Button(window, text=num[i][j], width=8, command=lambda x=num[i][j]: numButton(x))
        button.grid(column=j, row=i+2)

result = Button(window, text='=', width=8, command=calc)
result.grid(column=0, row=1, columnspan=1)

window.mainloop()
