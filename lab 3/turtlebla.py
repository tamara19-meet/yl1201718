import turtle
turtle.speed(100)
turtle.pensize(10)
a=20
for i in range (4):
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
	turtle.left(90)

turtle.register_shape("pentagon",((0,0), (50,0), (50,-50), (25,-75), (0,-50)))
turtle.shape("pentagon")



	
turtle.mainloop()