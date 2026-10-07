from turtle import *


# lightning bolt!!!
# right side-bottom section
pensize(4)
penup()
goto(0, -100)
pendown()
begin_fill()
left(55)
forward(110)
left(125)
forward(25)


# right-middle section
right(125)
forward(60)
left(125)
forward(25)


# right-top section
right(125)
forward(70)
left(125)
# top line
forward(60)


# left-top section
left(65)
forward(75)
left(115)
forward(20)


# left-middle section
right(115)
forward(60)
left(120)
forward(25)


# left-bottom section
right(110)
forward(80)
color("gold")
end_fill()


hideturtle()


done()
