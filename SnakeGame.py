#############################################
#  Snake Game using Python's Turtle Module  #
#############################################

import turtle
import time
import random

delay = 0.1

# scores
score = 0
high_score = 0


""" Set up the screen """
# create a window
win = turtle.Screen()

# giving the window a name
win.title("Snake Game")

# setting the background color for the window
win.bgcolor("grey")

# setting the height and width of the window
win.setup(width=600, height=600)

# window.tracer() turns of the screen updates
win.tracer(0)


""" Snake head """
# creating a turtle and assigning name head
head = turtle.Turtle()
head.speed(0)

# initializing head shape and color
head.shape("square")
head.color("black")

# turtle_name.penup() makes sure that the path taken by the snake is not drawn
head.penup()

# setting the position of the snakehead to the center
head.goto(0, 0)

# setting th e direction to "stop"
head.direction = "stop"


""" Snake food """
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
# food.shapesize(0.50, 0.50)
food.goto(0, 100)


segments = []


""" Add Scores """
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


""" Functions to move the snake """
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()     # y coordinate of the turtle
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()     # y coordinate of the turtle
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()     # x coordinate of the turtle
        head.setx(x + 20)
    
    if head.direction == "left":
        x = head.xcor()     # x coordinate of the turtle
        head.setx(x - 20)


""" Keyboard bindings """
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")


""" Main game loop """
while True:
    win.update()    # updates the screen continuously with the loop


    # Check for collision with border area
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
    
        # Hide the segments
        for segment in segments:
           segment.goto(1000, 1000) # out of range
 
        # clear segment list
        segments.clear()

        # reset score
        score = 0

        # reset delay
        delay = 0.1

        # update score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # calculating distance between the two objects
    # If the distance is less than 15(food and head come in contact), 
    # the food is re-positioned to a random position anywhere within the window
    if head.distance(food) < 15:
        # move the food to a random position on the screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        
        # add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001

        # increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        # update score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # move the end segment in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        
    
    # move segment 0 to where the head is 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
   
    move()


    # Check for head collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear segment list
            segments.clear()

            score = 0
            delay = 0.1

            # update score
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        
    time.sleep(delay) # to reduce the turtle speed


win.mainloop()