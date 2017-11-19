from turtle import *
class Square(Turtle):
	def __init__(self,shapesize):
		Turtle.__init__(self)
		self.shapesize(shapesize)
		self.random_colorshape("square")
	def random_color(self):
		r=random.randint(0,255)
		g=random.randint(0,255)
		b=random.randint(0,255)
		self.color()

sqaure1=Square(10)
mainloop()