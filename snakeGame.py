#Hussain Alhassan- Snake Head and Parameters
import turtle
import time
import random

delay = 0.1


score = 0
highScore = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

head = turtle.Turtle()
head.color("black")
head.shape("square")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"


#Sabrin Yasmin - create food object
#Snake food object
f_object = turtle.Turtle()
f_object.color("yellow")
f_object.shape("square")
f_object.speed(0)
f_object.penup()
f_object.goto(0,100)

tails = []

#Olivia Jackson - how score bar looks
pen = turtle.Turtle()
pen.color("purple")
pen.shape("square")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0, High Score: 0", align = "center", font=("Courier", 28, "normal")) 
    
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
wn.onkey(move_up, "w")
wn.onkey(move_down, "s")
wn.onkey(move_left, "a")
wn.onkey(move_right, "d")

#Sabrin Yasmnin - Main game loop
while True:
    wn.update()
    #Archita Govindarajan
    #Check for collison with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        #To hide tails
        for tail in tails:
            tail.goto(1000,1000)
            
        #To clear tails list
        del tails [:]
       
        #Olivia Jackson - collides with sides 
        score = 0
       
        delay = 0.1
        
        pen.clear
        pen.write("Score: {}  High Score: {}".format(score,highScore), align = "center",font =("Courier", 28, "normal"))

    if head.distance(f_object) < 18:
        # Move the f_object to 
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        f_object.goto(x,y)


        #Add a tail video 4
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("red")
        new_tail.penup()
        tails.append(new_tail)

        #Olivia Jackson - how score increases
        delay -= .001
    
        score += 1
        
        if score > highScore:
            highScore = score
            
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,highScore), align = "center",font =("Courier", 28, "normal"))
        
        
    #Move the end tails first in reverse order  video 4
    for index in range(len(tails)-1, 0, -1):
        x = tails [index-1].xcor()
        y = tails [index-1].ycor()
        tails[index].goto(x,y)


    #Move tail 0 to where the head is  video 4
    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0]. goto(x,y)
        
    move()
    
    # Archita to check for head collison with the body
    for tail in tails:
        if tail.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
           
            #To hide tails
            for tail in tails:
                tail.goto(1000,1000)
            
            #To clear tails list
            tails.clear()

            #Olivia Jackson - collides with self/tail 
            score = 0
            
            delay = .1
            
            pen.clear
            pen.write("Score: {}  High Score: {}".format(score,highScore), align = "center",font =("Courier", 28, "normal"))

#Hussain Alhassan- Time Delay

    time.sleep(delay)

wn.mainloop()
