from turtle import*

setup(1.0,1.0)

up()
goto(-550,250)

kol=0
while kol<10:
    down()
    for i in range(4):
        fd(100)
        lt(90)
    up()
    fd(120)
    kol+=1
goto(-550,50)
kol=0
while kol<10:
    down()
    for i in range(3):
        fd(100)
        lt(120)
    up()
    fd(120)
    kol+=1
mainloop()

    


