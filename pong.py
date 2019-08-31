import turtle
from ball import *
from player import *

window = turtle.Screen()
window.bgcolor("navy blue")
window.setup(width=1000, height=800)
window.title("Pong Game!")
window.tracer(0)


window.listen()

window.onkeypress(playerOneMoveUp, "w")
window.onkeypress(playerTwoMoveUp, "Up")

window.onkeypress(playerOneMoveDown, "s")
window.onkeypress(playerTwoMoveDown, "Down")



def xSatisfiedPlayerTwo():
	return getX() > 450 and getX() < 460

def ySatisfiedPlayerTwo():
	return getY() > getPlayerTwoY() - 80 and getY() < getPlayerTwoY() + 80


def xSatisfiedPlayerOne():
	return getX() < -450 and getX() > -460

def ySatisfiedPlayerOne():
	return getY() > getPlayerOneY() - 80 and getY() < getPlayerOneY() + 80


def checkCollisions():
	if (xSatisfiedPlayerTwo() == True and ySatisfiedPlayerTwo() == True):
		setX(450)
		reverseDirectionX()

	elif (xSatisfiedPlayerOne() == True and ySatisfiedPlayerOne() == True):
		setX(-450)
		reverseDirectionX()

while True:
	window.update() 

	updateX()
	updateY()

	checkCoordinates()

	checkCollisions()