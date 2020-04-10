
import turtle 
import time

import random

delay = 0.2

score = 0
hiegh_score= 0

#create a sreen 

wn = turtle.Screen()
wn.title("snak game that i made")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#create the head of the warm 

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "none"



#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

#keyborad bindings

#make it move 
#make functions for moving 
def go_stop():



		head.direction="stop"

def go_up():
	if head.direction != "down":
	   head.direction = "up"

def go_down():
	if head.direction != "up":
	  head.direction = "down"

def go_left():
	if head.direction != "right":
		head.direction = "left"

def go_right():
	if head.direction != "left":

		head.direction = "right"

wn.listen()
wn.onkeypress(go_stop,"k")

wn.onkeypress(go_up,"w")

wn.onkeypress(go_down,"s")

wn.onkeypress(go_left,"a")

wn.onkeypress(go_right,"d")


def move():


	if head.direction == "stop":
		y= head.ycor()
		head.sety(y - 1)



	if head.direction == "up":

		y = head.ycor()
		head.sety(y + 20)


	if head.direction == "down":

		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":

		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":

		x = head.xcor()
		head.setx(x + 20)


     




while True:
	
	wn.update()

	#ckek for colosion with the border

	if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
		time.sleep(1)
		head.goto(0,0)
		head.direction = "stop"


		# hide the segments

		for segment in segments:

			segment.goto(1000,1000)

		segments.clear()
		
	#ckeck for a collision with food

	if head.distance(food)<20:
		score += 1
		#move the food random spot
		x = random.randint(-290,290)
		y = random.randint(-290,290)
		food.goto(y,x)

		# Add a segment 
		
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("grey")
		new_segment.penup()
		segments.append(new_segment)

		score+=10
		if score> hiegh_score:
			hiegh_score=score

		pen.clear()

		pen.write("Score : {}   Hieh_Score : {}".format(score,hiegh_score),align="center",font=("normal ",24))

		


	#move the end segments first in reverse
	for index in range(len(segments)-1,0,-1):
		x = segments[index-1].xcor()

		y = segments[index-1].ycor()

		segments[index].goto(x,y)


	#move segment 0 to where the head is 
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()

		segments[0].goto(x,y)



	



		

	
	move()
	#check for head collision with the body segments
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0,0)
			head.direction = "stop"

			# hide the segments

			for segment in segments:

				segment.goto(1000,1000)

			segments.clear()

	

	time.sleep(delay)

	#ckeck for a collision with food






	




	
wn.mainloop()