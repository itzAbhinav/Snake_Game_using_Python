import turtle
import random
import time

# create screen 
screen = turtle.Screen()
screen.title(" SNAKE GAME ")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# create border 
turtle.speed(4)
turtle.pensize(5)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.penup()
turtle.hideturtle()

# Score 
score = 0
delay = 0.1 

# snake 
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("yellow")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

# food 
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("pink")
food.penup()
food.goto(60,60)

old_food = []

# Scoring 
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.goto(0,300)
scoring.write("Score: ", align="center", font=("Courier",24,"bold") )

# snake movements 

def go_up():
    if snake.direction != "down":
        snake.direction = "up"
def go_down():
    if snake.direction != "up":
        snake.direction = "down"
def go_left():
    if snake.direction != "right":
        snake.direction = "left"
def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    elif snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    elif snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
    elif snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

# keyboard binding 
screen.listen()
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")

# Main loop 
while True:
    screen.update()

    if snake.distance(food) < 20:
        x = random.randint(-290,270)
        y = random.randint(-240,240)
        food.goto(x,y)
        scoring.clear()
        score += 1
        scoring.write(f"Score: {score}" , align="center", font=("Courier",24,"bold"))
        delay -= 0.001

        # creating new foods 
        new_food = turtle.Turtle()
        new_food.speed(0)
        new_food.shape("square")
        new_food.color("orange")
        new_food.penup()
        old_food.append(new_food)
    
    # adding len to snake 

    for idx in range(len(old_food) - 1,0,-1):
        a = old_food[idx - 1].xcor()
        b = old_food[idx - 1].ycor()
        old_food[idx].goto(a,b)
    
    if len(old_food) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_food[0].goto(a,b)
    
    move()

    # snake & border collision 

    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0,0)
        scoring.write(f"  Game Over \n Your score is {score}",align="center", font=("Courier",30,"bold"))

    # snake collision 
    for idx in old_food:
        if idx.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0,0)
            scoring.write(f"  Game Over \n Your score is {score}",align="center", font=("Courier",30,"bold"))

    time.sleep(delay)

turtle.Terminator()



