import turtle

def draw_square(brad):
	for i in range(0, 4):
		brad.forward(100)
		brad.right(90)
	
def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
#	brad.speed(2)

	for times in range (0, 37):
		draw_square(brad)
		brad.right(10)

#	angie = turtle.Turtle()
#	angie.shape("arrow")
#	angie.color("blue")
#	angie.circle(100)
#
#	kappa = turtle.Turtle()
#	kappa.shape("triangle")
#	kappa.color("black")
#	for times in range(0, 3):
#		kappa.forward(100)
#		kappa.left(120)

	window.exitonclick()

draw_art()
