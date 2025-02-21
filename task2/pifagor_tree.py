import turtle
import math

def draw_pythagoras_tree(branch_length, depth):
    if depth == 0:
        return
    turtle.forward(branch_length)

    position = turtle.pos()
    angle = turtle.heading()

    # left part
    turtle.left(45)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, depth - 1)

    turtle.setpos(position)
    turtle.setheading(angle)

    # right part
    turtle.right(45)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, depth - 1)

    # return
    turtle.setpos(position)
    turtle.setheading(angle)

# setup Turtle
turtle.speed("fastest")
turtle.color("red")
turtle.left(90)
turtle.up()
turtle.goto(0, -200)
turtle.down()

# Викликаємо функцію
user_inp = input("Введіть глибину дерева: ")
while not user_inp.isdigit():
    user_inp = input("Введіть глибину дерева: ")
d = int(user_inp)
br_len = 100
draw_pythagoras_tree(br_len,d)  # Глибина рекурсії = 10

# Завершуємо малювання
turtle.done()