import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.color("red")
t.speed(1000)  # Velocidad 

t.fillcolor("red")
t.begin_fill()

t.left(140)
t.forward(113)

for _ in range(200):
    t.right(1)
    t.forward(1)

t.left(120)

for _ in range(200):
    t.right(1)
    t.forward(1)

t.forward(112)

t.end_fill()

# Luego de terminar el dibujo, escribe el mensaje
t.setpos(0, -22)
t.color("white")
t.write("Feliz Día", align="center", font=("Arial", 16, "bold"))

# Ahora sí oculta la tortuga
t.hideturtle()

turtle.done()

