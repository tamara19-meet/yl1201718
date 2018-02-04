from turtle import *

import time
import random
from ball import Ball
tracer(0)
# hideturtle()
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=getcanvas().winfo_width()/2
SCREEN_HEIGHT=getcanvas().winfo_height()/2
register_shape("tm.gif")
color("pink")
# dot(1000)
write("Agario", align="center", font=("Arial",150))


my_ball=Ball(100,0,0,0,20,"black")
NUMBER_OF_BALLS = 8
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 35
MINIMUM_BALL_DX = -2
MAXIMUM_BALL_DX = 2
MINIMUM_BALL_DY = -2
MAXIMUM_BALL_DY = 2	
BALLS=[]

#life:
showturtle()
life=clone()
life.shape("tm.gif")
life.penup()
life.goto(100,200)
life2=life.clone()
life2.goto(150,200)
life3=life.clone()
life3.goto(200,200)
hideturtle()
getscreen().update()	




for i in range(NUMBER_OF_BALLS):

	x=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
	y=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
	dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
	dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))
	r=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
	color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))

	while dx==0:
		dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
	while dy==0:
		dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))


	NEW_BALL=Ball(x,y,dx,dy,r,color)
	BALLS.append(NEW_BALL)



def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)



def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	b1y=ball_a.ycor()
	b2y=ball_b.ycor()
	b1x=ball_a.xcor()
	b2x=ball_b.xcor()
	b1r=ball_a.r
	b2r=ball_b.r
	sr=b1r+b2r
	d=((b2x-b1x)**2+(b2y-b1y)**2)**0.5
	if d<=sr:
		return True
	else:
		return False
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b)== True:

				radius1=ball_a.r
				radius2=ball_b.r

				if radius1>radius2:
					ball_a.r=radius1+1

					x=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
					y=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
					dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
					dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))
					r=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
					color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))


					while dx==0:
						dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
					while dy==0:
						dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))


					ball_b.goto(x,y)
					ball_b.dx=dx
					ball_b.dy=dy
					ball_b.r=r
					ball_b.color(color)
					ball_b.shapesize(r/10)
					ball_a.shapesize(ball_a.r/10)

				if radius1<radius2:
					ball_b.r=radius2+1
					x=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
					y=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
					dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
					dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))
					r=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
					color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))


					while dx==0:
						dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
					while dy==0:
						dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))


					ball_a.goto(x,y)
					ball_a.dx=dx
					ball_a.dy=dy
					ball_a.color(color)
					ball_a.shapesize(r/10)
					ball_b.shapesize(ball_b.r/10)



def check_myball_collision():
	for i in BALLS:
		if collide(my_ball,i)==True:
			radius1=my_ball.r
			radius2=i.r
			if radius1<radius2:
				return False
			else:
					my_ball.r=radius1+1
					x=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
					y=random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
					dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
					dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))
					r=random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
					color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))


					while dx==0:
						dx=random.randint(int(MINIMUM_BALL_DX ),int (MAXIMUM_BALL_DX))
					while dy==0:
						dy=random.randint(int(MINIMUM_BALL_DY ),int (MAXIMUM_BALL_DY))



					i.goto(x,y)
					i.dx=dx
					i.dy=dy
					i.r=r
					i.color(color)
					i.shapesize(r/10)
					radius1+=1
					my_ball.shapesize(radius1/10)
	return True

def movearound(event):
	my_ball.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)

getcanvas().bind("<Motion>", movearound)
getscreen().listen()

def score():
	score_turtle=Turtle()
	score_turtle.hideturtle
	score_turtle.clear()
	score_turtle.pu()
	score_turtle.color("black")
	score_turtle.goto(-200, 200)
	score_turtle.write("Score: " + str((my_ball.r-20)+1), font=("Arial", 16, "normal"))
	score_turtle.clear()


while RUNNING == True:
	if SCREEN_WIDTH != getcanvas().winfo_width()/2 or SCREEN_HEIGHT!=getcanvas().winfo_height()/2:
		SCREEN_WIDTH = getcanvas().winfo_width()/2 
		SCREEN_HEIGHT=getcanvas().winfo_height()/2
	move_all_balls()
	if check_myball_collision()==False:
		if life_counter==3:
			life.hideturtle()
			life_counter-=1
		if life_counter==2:
			hideturtle()
			life_counter-=1
		if life_counter==1:
			life3.hudeturtle()
			life_counter-=1
			RUNNING=False
	check_all_balls_collision()
	# my_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	RUNNING = check_myball_collision()
	update()
	time.sleep(SLEEP)
	score()


if RUNNING==False:
	write("GAME OVER",align="center",font=("Arial",50))
	







mainloop()






