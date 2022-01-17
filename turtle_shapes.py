import turtle

t = turtle.Turtle()

turtle.pen()

colors = ['purple', 'red', 'orange', 'blue', 'green']
turtle.bgcolor('white')

for i in range(200):
    t.color(colors[i % 5])
    t.pensize(int(i / 10 + 1))
    t.forward(i)
    t.left(59)

turtle.done()
