import tkinter as tk

calc = tk.Tk()
calc.title('My calulator')

buttons = [
    '7', '8', '9', '*', 'C',
    '4', '5', '6', '/', 'Neg',
    '1', '2', '3', '-', '$',
    '0', ',', '=', '+', '@'    
]

row = 1
col = 1

for i in buttons:
    action = lambda x = i: click_event(x)
    tk.Button(calc, text=i, font=('Arial', 10, 'bold'), bg='#f5f5f5', fg='#111', activebackground='#f5f5f5', activeforeground='#111', bd=3, width=5, height=5, command=action) \
    .grid(row = row, column = col , padx=5, pady=5)
    
    col += 1
    
    if col > 4:
        col = 0
        row += 1
            
    display = tk.Entry(calc, width=40, bg="white")
    display.grid(row= 0, column= 0, columnspan=5)
        
    def click_event(key):
        if key == "=":
            if '/' in display.get() and '.' not in display.get():
                display.insert(tk.END, ".0")
                
            try:
                result = eval(display.get())
                display.insert(tk.END, " = " + str(result))
            except:
                display.insert(tk.END, "Use only valid characters")
                
        elif key == "C":
            display.delete(0, tk.END)
            
        elif key == "$":
            display.delete(0, tk.END)
            display.insert(tk.END, "$")
                
        elif key == "@":
            display.delete(0, tk.END)
            display.insert(tk.END, "@")
            
        elif key == "Neg":
            if "=" in display.get():
                display.delete(0, tk.END)
            try:
                if display.get()[0] == "-":
                    display.delete(0)
                else:
                    display.insert(0, '-')
            except IndexError:
                pass
        
        else:
            if '=' in display.get():
                display.delete(0, tk.END)
            display.insert(tk.END, key)
            
calc.mainloop()
            
            
    
                
