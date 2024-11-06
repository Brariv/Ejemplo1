from turtle import *
import random
hideturtle()
setup(500, 530, -100, 100)
a = "Cuadrado!"

bgcolor("black")
pencolor("white")
# write(a, font = ("Arial", 20, "bold"))
def interfaz1():
	home()
	clear()
	bgcolor("black")
	pencolor("white")
	penup()
	goto(0,15)
	pendown()
	begin_fill()
	fillcolor("green")
	circle(80)
	end_fill()
	penup()
	backward(90)
	right(90)
	forward(50)
	write("Spotify UVG", font = ("Arial", 23, "bold"))
	forward(50)
	write("1. Agregar nueva canción", font = ("Arial", 10))
	forward(20)
	write("2. Eliminar canción", font = ("Arial", 10))
	forward(20)
	write("3. Ver canciones guardadas", font = ("Arial", 10))
	forward(20)
	write("4. Ver artistas guardados", font = ("Arial", 10))
	forward(20)
	write("5. Eliminar todas las canciones", font = ("Arial", 10))
	forward(20)
	write("6. Salir", font = ("Arial", 10))
	forward(20)


def interfaz2(c,datos):
	home()
	clear()
	bgcolor("black")
	pencolor("white")
	penup()
	goto(-230,210)
	write("Canciones Guardadas", font = ("Arial", 23, "bold"))
	right(90)
	forward(30)
	write("Cancion \t Album \t Artista \t\t Duracion", font = ("Arial", 12))
	forward(30)
	for i in range(c):
		key, value = list(datos.items())[i]
		a = key + "\t " + value[0] + "\t " + value[1] + "\t\t" + str(value[2]) + ":" + str(value[3])
		write(a, font = ("Arial", 12))
		forward(20)

def cuadroA(a,c):
	v = "Canciones: " + str(c)
	pencolor("white")
	color = "#"
	for j in range(6):
		char = random.choice('0123456789ABCDEF')
		color = color + char
	for i in range(2):
		forward(100)
		right(90)
		forward(150)
		right(90)
	penup()
	forward(10)
	right(90)
	forward(50)
	pendown()
	begin_fill()
	fillcolor(color)
	circle(40)
	end_fill()
	penup()
	forward(70)
	write(a, font = ("Arial", 11, "bold"))
	forward(20)
	write(str(v), font = ("Arial", 10))
	backward(140)
	left(90)
	forward(90)

def fila(a,v,datos):
	for i in range(a,v):
		key, value = list(datos.items())[i]
		cuadroA(key,value)
		forward(20)
		pendown()

def interfaz3(c,datos):
	home()
	clear()
	bgcolor("black")
	penup()
	if (c <= 4):
		goto(-230,250)
		pendown()
		fila(0,c,datos)
	elif (c <= 8):
		goto(-230,250)
		pendown()
		fila(0,4,datos)
		penup()
		goto(-230,80)
		pendown()
		fila(4,c,datos)
	else:
		goto(-230,250)
		pendown()
		fila(0,4,datos)
		penup()
		goto(-230,80)
		pendown()
		fila(4,8,datos)
		penup()
		goto(-230,-90)
		pendown()
		fila(8,c,datos)