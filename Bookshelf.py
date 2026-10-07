# star imports everything
from turtle import *




shape("turtle")
pensize(3)


print(pos())


bgcolor("#A1867F")


# square
for i in range(4):
    forward(50) # pixels
    left(90)


# title
color("#F2EDEB")
penup()
goto(-300, 300)
pendown()
write("Tracy's Book Shelf!! (≧◡≦)", font=("Courier", 30, "bold"))


# book shelf-back


penup()
goto(-250, 255)
forward(30)
pendown()


color("#4A2511")
begin_fill()
for i in range(2):
    forward(500)
    right(90)
    forward(600)
    right(90)
end_fill()


# Book shelf details--rectangles/round sjhfo


penup()
goto(-248, 255)




# writing dictbooks


#keeps the window open
done()
