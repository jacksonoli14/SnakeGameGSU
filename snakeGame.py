
#Hussain Alhassan- Snake Head and Parameters
import turtle
import time
import random

delay = 0.1


score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Olivia Jackson - how score bar looks - line 37ish
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("purple")
pen.penup()
pen.hideturtle()
pen.goto(1,260)
pen.write("Score: 0, High Score: 0", align = "center",font =("Ariel", 28, "bold"))

#Hussain Alhassan- Directions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def move_down():
    if head.direction != "up":
        head.direction = "down"


def move_left():
    if head.direction != "right":
        head.direction = "left"


def move_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#Olivia Jackson - how score increases
score += 1
if score > highScore:
  highScore = score
pen.clear
pen.write("Score: {}  High Score: {}".format(score,highScore), align = "center",font =("Ariel", 28, "bold"))


#Olivia Jackson - collides with sides t
score = 0
pen.clear
pen.write("Score: {}  High Score: {}".format(score,highScore), align = "center",font =("Ariel", 28, "bold"))


#Olivia Jackson - collides with self/tail 
score = 0
pen.clear
pen.write("Score: {}  High Score: {}".format(score,highScore), align = "center",font =("Ariel", 28, "bold"))

#Hussain Alhassan- Time Delay

time.sleep(delay)

wn.mainloop()
