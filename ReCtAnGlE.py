from turtle import *
import random
import math 

class rectangle(Turtle):
	def __init__(self, height, color, speed, Width):
		Turtle.__init__(self)
		self.shape("rectangle")
		self.shapesize(height)
		self.color(color)
		self.speed(speed)