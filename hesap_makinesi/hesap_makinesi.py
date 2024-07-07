import tkinter as tk
#sayı giriş kısmını temizlemek için oluşturulan fonksiyon
def clear_entry():
    entry.delete(0,tk.END)
#girilen sayının içe aktarılmasını sağlayan fonksiyon
def add_entry(button):
    entry.insert(tk.END,button)
#evaluate fonksiyonu girilen işlemleri algılayıp uygun sonucu verir
def evaluate():
    try:
        expression = entry.get()
        if '%' in expression:
            parts = expression.split('%')
            if len(parts) == 2:
                base = float(parts[0])
                percent = float(parts[1])
                result = base * percent/100
                entry.delete(0,tk.END)
                entry.insert(tk.END,str(result))
                return
        result = eval(expression)
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    except:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"Hata")
                 
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
    if button == 'C':
        action = clear_entry
    elif button == '=':
        action = evaluate
    else:
        action = lambda b=button: add_entry(b)
    tk.Button(window,text=button,padx=14.3,pady=14.3,command=action).grid(row=row_val,column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
