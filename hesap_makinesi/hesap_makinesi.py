import tkinter as tk

window = tk.Tk()
window.title("Hesap Makinesi")
window.geometry("300x300")

entry = tk.Entry(window)
entry.grid(row=0,column=0,columnspan=4)

buttons = [
    '(',')','%','C',
    '7','8','9','/',
    '6','5','4','*',
    '3','2','1','-',
    '0','.','=','+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window,text=button,padx=14.3,pady=14.3).grid(row=row_val,column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
