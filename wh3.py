from turtle import*

setup(1.0,1.0)
speed(0)

color('green')
width(4)
shape('turtle')
a=5
while True:
    for i1 in range(5):
        for j in range(20):
            for i in range(4):
                fd(200)
                lt(90)
            lt(a)
        clear()
        a+=10





mainloop()



    




