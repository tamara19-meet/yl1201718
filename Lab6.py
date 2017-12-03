from turtle import *
import turtle
import random
import math 

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)

ball1= Ball(10,"Green", 5)
ball2= Ball(7,"Orange",5)
ball1_x= ball1.xcor()
ball1_y= ball1.ycor()
ball2_x= ball1.xcor()
ball2_y= ball1.ycor()
def check_collision(ball1,ball2):
	if ball.shapesize() + ball2.shapesize() > (((ball2_x-ball_x)^2) + (ball2_y-ball_y)^2)*0.5:
		print("f")

turtle.mainloop()
