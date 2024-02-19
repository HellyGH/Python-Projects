import turtle
import random

# Set up the screen
t = turtle.Screen()
t.bgcolor("yellow")

# Create the snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("red")
snake.speed(0)
snake.penup()
snake.hideturtle()

# Create the leaf
leaf = turtle.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
leaf.shape("turtle")
leaf.color("green")
leaf.penup()
leaf.speed(0)

# Set up game state variables
game_started = False
score = 0

# Create text turtle for displaying messages
text_turtle = turtle.Turtle()
text_turtle.write("Press Space to start", align="center", font=('Arial', 16, "bold"))
text_turtle.hideturtle()

# Create score turtle
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

# Define movement functions
def move_up():
    if snake.heading() != 270:
        snake.setheading(90)

def move_down():
    if snake.heading() != 90:
        snake.setheading(270)

def move_right():
    if snake.heading() != 180:
        snake.setheading(0)

def move_left():
    if snake.heading() != 0:
        snake.setheading(180)

# Define function to check if snake is outside window
def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = snake.pos()
    return x < left_wall or x > right_wall or y < bottom_wall or y > top_wall

# Define function to display game over message
def game_over():
    snake.color('yellow')
    leaf.color('yellow')
    text_turtle.penup()
    text_turtle.goto(0, 0)
    text_turtle.write('Game Over', align='center', font=('Arial', 30, 'normal'))

# Define function to display score
def display_score():
    score_turtle.clear()
    score_turtle.penup()
    score_turtle.goto(t.window_width() / 2 - 50, t.window_height() / 2 - 50)
    score_turtle.write(str(score), align='right', font=('Arial', 40, 'bold'))

# Define function to place leaf
def place_leaf():
    leaf.goto(random.randint(-200, 200), random.randint(-200, 200))

# Define function to start game
def start_game():
    global game_started, score
    if not game_started:
        game_started = True
        score = 0
        text_turtle.clear()
        snake_speed = 2
        snake_length = 3
        snake.shapesize(1, snake_length, 1)
        snake.showturtle()
        display_score()
        place_leaf()
        while True:
            snake.forward(snake_speed)
            if snake.distance(leaf) < 20:
                place_leaf()
                snake_length += 1
                snake.shapesize(1, snake_length, 1)
                snake_speed += 1
                score += 10
                display_score()
            if outside_window():
                game_over()
                break

# Bind keys to functions
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_right, 'Right')
t.onkey(move_left, 'Left')
t.listen()
t.mainloop()