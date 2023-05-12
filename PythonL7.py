from tkinter import

root = Tk()
root.geometry('400x500')

dates = []

def add():
    global dates










































Entry(frame, textvariable=Name, width=50).pack()

Label(frame1, text='Number').pack(side=Left)
Entry(frame1, textvariable=Number, width=50),pack()

Label(frame2, text='Address').pack(side=Left)
Address = Text(frame2, width=40, height=10)
Address.pack()

Button(root, text= 'Add', command=add).place(x=100, y=270)
Button(root, text= 'View', command=view).place(x=100, y=310)
Button(root, text= 'Delete', command=delete).place(x=100, y=350)
Button(root, text= 'Reset', command=reset).place(x=100, y=390)

select = Listbox(root, height=12)
select.place(x=200, y=260)
select.pack()

root.mainloop()
