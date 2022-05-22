import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0


#set up the screen 
window = turtle.Screen()
window.title("Snake Game By MD RAIHANUL KABIR RAFI")                # Title for the game
window.bgcolor("sky blue")                                          # Background color as sky blue 
window.setup(width=600, height=600)                                 # Setting up the size for the window
window.tracer(0)                                                    # Turn off the Screen updates

#Snake Head
head = turtle.Turtle()
head.speed(0)                                                       # Animation speed of the turtle module
head.shape("square")                                                
head.color("black")
head.penup()                                                        # So that it doesn't draw anything
head.goto(0,0)
head.position = "stop"                                              # When it will start it will stay in the middle

#Snake Food                                                         # We did everything same as snake head expect for "head.position" cause food doesn't move like the snake does
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()                                                        # so that it doesn't draw anything
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0     High Score: 0", align="center", font=("Algerian", 24, "normal"))

# Functions
def go_up():
    if head.position != "down":
        head.position = "up"

def go_down():
    if head.position != "up":
        head.position = "down"

def go_right():
    if head.position != "left":
        head.position = "right"

def go_left():
    if head.position != "right":
        head.position = "left"

def move():
    if head.position == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.position == "down":
        y = head.ycor()
        head.sety(y - 20)
                                                                    # defined the moves
    if head.position == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.position == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard Bindings
window.listen()                                                     # Listen for key presses
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_right, "Right")                                # We can move the into different direction using snake using arrow key
window.onkeypress(go_left, "Left")

window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_right, "d")                                    # We can move the snake into different direction using (W,S,A,D) as well 
window.onkeypress(go_left, "a")

# Main game loop
while True:
    window.update()                                                 # It will update the screen 

    # Check for a Collision with the "Border"
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.position = "stop"

        # Hide the segments
        for segment in segments:                                    
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Algerian", 24, "normal"))                   

        
    # Check the collision with the "Food"
    if head.distance(food) < 20:
        # Move the food to a different spot
        x = random.randint(-290,290)                                        # So that it doesn't go out the screen
        y = random.randint(-290,290)
        food.goto(x,y)

        # Add a segment or body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment) 

        # Shorten the delay
        delay -= 0.001                                              # When the snake will longer the speed will automatically increased to make it more challenging 

        # Increase the score 
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Algerian", 24, "normal"))                   

    # Move the end segment first in "Reverse order"
    for index in range(len(segments)-1,0,-1):                               # Add new segments for the snake when it will eat the food
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.position = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1                                         # When the snake will die, it will reset the shorten and back to normal speed again

            # Update the score delay
            pen.clear()                                         # To clear the overwrite of the score
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Algerian", 24, "normal"))                   



    time.sleep(delay)

window.mainloop()                                               # It basically keep the window open for us