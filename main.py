from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

screen.listen()

def move_fwd():
    tim.forward(10)

def move_bwd():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(move_fwd, "w")
screen.onkey(move_bwd, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()