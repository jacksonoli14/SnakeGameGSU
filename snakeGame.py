
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

#Sabrin Yasmin - create food object
#Snake food object
f_object = turtle.Turtle()
f_object.color("yellow")
f_object.shape("square")
f_object.speed(0)
f_object.penup()
f_object.goto(0.100)

tails = []

#Hussain Alhassan- Directions
def move_up():
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
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")

#Sabrin Yasmnin - Main game loop
while True:
    wn.update()

    if head.distance(f_object) < 18
        # Move the f_object to 
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        f_object.goto(x,y)


        #Add a segment video 4
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("red")
        new_tail.penup()
        tails.append(new_tail)

    #Move the end tails first in reverse order  video 4
    for index in range(len(tails)-1, 0, -1):
        x = tails {index-1}.xcor()
        y = tails {index-1}.ycor()
        tails{index}.goto(x,y)


    #Move tail 0 to where the head is  video 4
    if lef(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0]. goto(x,y)
        
    move()

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
