from turtle import *
import random
import math 

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

ball1= Ball(5,"Red", 1)
ball2= Ball(12,"Green",5)

ball1.forward(10)
ball2.backward(10)

def check_collision(ball1,ball2):
	D = math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2) + math.pow((ball1.ycor()-ball2.ycor()),2))

	if (D<ball1.radius + ball2.radius):
		print("collision")

check_collision(ball1,ball2)
ball1.backward(5)
ball2.backward(5)
check_collision(ball1,ball2)
balls = [ball1,ball2]
def checking(banana, size):

	numbers = []
	for i in range (size):
		numbers.append(i)
	i=0
	D= math.sqrt(math.pow((banana[i].xcor()-banana[i+1].xcor()),2) + math.pow((banana[i].ycor()-banana[i+1].ycor()),2))
	if (D < banana[0].radius + banana[1].radius):
		print("collision 1")
checking(balls,2)

mainloop()
