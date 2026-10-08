# star imports everything
from turtle import *




shape("turtle")
pensize(3)
speed(15)

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
goto(-250, 255)
forward(30)
pensize(10)
color("#231709")
pendown()

for i in range(2):
    forward(500)
    right(90)
    forward(600)
    right(90)

# writing dictbooks

books = {
    "The Westing Game" : "Ellen Raskin",
    "Doll Bones" : "Hobby Black",
    "FNAF: Fazbear Frights #1: Into the Pit" : "Scott Cawthon",
    "The Outsiders" : "S.E. Hinton",
    "Of Mice and Men" : "John Steinbeck",
    "Goosebumps" : "R.L. Stine",
    "A Series of Unfortunate Events" : "Lemony Snicket",
    "Solo" : "Kwame Alexander"
}

# show the books on the shelf

color("#F2EDEB")
penup()
goto(-170, 220)
pendown()

write(books, font = ("Courier", 14, "bold"))


#keeps the window open
done()
