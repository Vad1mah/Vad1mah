import turtle

screen = turtle.Screen()
screen.setup(1000,1000)
screen.tracer(0)


car = turtle.Turtle()
car.speed(0)
car.hideturtle()


def draw_car():
    car.pendown()
    car.color('green')
    car.begin_fill()
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.left(90)
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.end_fill()
    car.back(50)
    car.left(90)
    car.forward(70)
    car.left(90)
    car.begin_fill()
    car.forward(90)
    car.right(90)
    car.forward(230)
    car.right(90)
    car.forward(90)
    car.end_fill()
    car.color('black')
    car.right(90)
    car.forward(230)
    car.back(115)
    car.right(90)
    car.forward(90)
    car.penup()
    car.goto(x, 0)
    car.pendown()
    car.setheading(0)
    car.forward(70)
    car.right(180)
    car.pensize(3)
    car.circle(30)
    car.penup()
    car.left(90)
    car.forward(30)
    car.right(degree)
    car.pendown()

    for i in range(4):
        car.forward(30)
        car.penup()
        car.back(30)
        car.right(90)
        car.pendown()
    
    car.penup()
    car.goto(x, 0)
    car.setheading(0)
    car.forward(300)
    car.left(180)
    car.pendown()
    car.circle(30)
    car.penup()
    car.left(90)
    car.forward(30)
    car.right(degree)
    car.pendown()

    for i in range(4):
        car.forward(30)
        car.penup()
        car.back(30)
        car.right(90)
        car.pendown()
        
    car.penup()
    car.goto(x, 0)
    car.setheading(0)
    car.pensize(1)
    screen.update()
    car.forward(1)


x = -900
y = 0
degree = 0
car.penup()
car.goto(x, 0)
car.setheading(0)

while True :
    car.clear()
    draw_car()
    screen.update()
    car.forward(1)
    x += 2
    y += 2
    degree += 1
    if x == 900:
        x = -900
    if y == 360:
        y = 0


