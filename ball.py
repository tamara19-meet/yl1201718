from turtle import Turtle
import turtle
import random
import math
turtle.hideturtle()
turtle.colormode(255)
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(r/10)
		self.r = r
		self.color(color)
		self.dx=dx
		self.dy=dy
		# r=random.randint(0,255)
		# g=random.randint(0,255)
		# b=random.randint(0,255)
		# self.color(r,g,b)

	def move(self,screen_width,screen_height):
		
		current_x=self.xcor()
		current_y=self.ycor()
		new_x=current_x+self.dx
		new_y=current_y+self.dy
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		top_side_ball=new_y+self.r
		bottom_side_ball=new_y-self.r
		self.goto(new_x,new_y)



		if right_side_ball>screen_width:
			self.dx=-self.dx
		elif bottom_side_ball<-screen_height:
			self.dy=-self.dy
		elif left_side_ball<-screen_width:
			self.dx=-self.dx
		elif top_side_ball>screen_height:
			self.dy=-self.dy





		# def top(self):
		# 	return.self.ycor()+(0.5*self.height)
		# def bottom(self):
		# 	return.self.ycor()-(0.5*self.height)
		# def right(self):
		# 	return.self.xcor()+(o.5*self.width)
		# def left(self):
		# 	return.self.xcor()-(0.5*self.width)
		# if(A.top()>B.bottom()and A.right()>B.left()and A.bottom()<B.top()and A.left()>B.right()):
