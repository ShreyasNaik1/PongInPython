from util import *
import random
from score import *

ball = turtle.Turtle()
createObject(ball)
ball.shape("circle")
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1



def getX():
	return ball.xcor()

def getY():
	return ball.ycor()

def setX(n):
	ball.setx(n)

def setY(n):
	ball.sety(n)



def getSpeedX():
	return ball.dx

def getSpeedY():
	return ball.dy

def reverseDirectionX(): 
	ball.dx *= -1 

def reverseDirectionY(): 
	ball.dy *= -1 




def resetBall():
	ball.goto(0, 0) 


def randomSpeed():
	ball.dx = random.randint(10, 29) / 100 if ball.dx < 0 else -(random.randint(10, 29) / 100)



def getBallWidth():
	return ball.width()




def updateX(): 
	setX(getX() + getSpeedX())

def updateY(): 
	setY(getY() + getSpeedY())


def dealWithY(n):
	setY(n)
	reverseDirectionY()

def dealWithX(player):
	resetBall()
	randomSpeed()
	if (player == True):
		increaseScoreOfOne()
	else: 
		increaseScoreOfTwo()
	clear()		
	writeScore(getScoreOne(), getScoreTwo())


def checkCoordinates():
	if (getY() > 380):
		dealWithY(380)
		
	if (getY() < -380):
		dealWithY(-380)

	if (getX() > 480):
		dealWithX(True)

	if (getX() < -480):
		dealWithX(False)