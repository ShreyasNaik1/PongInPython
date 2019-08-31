from util import *
import turtle

playerOne = turtle.Turtle()
createObject(playerOne)
playerOne.shapesize(stretch_wid=8, stretch_len=1)
playerOne.goto(-460, 0)

playerTwo = turtle.Turtle()
createObject(playerTwo)	
playerTwo.shapesize(stretch_wid=8, stretch_len=1)
playerTwo.goto(460, 0)


def playerMove(player, direction):
	y = player.ycor()
	if (direction == True):
		if (y < 475 - 175):
			y += 25
			player.sety(y)
	else: 
		if (y > -475 + 175):
			y -= 25
			player.sety(y) 



def playerOneMoveUp():
	playerMove(playerOne, True)

def playerTwoMoveUp():
	playerMove(playerTwo, True)

def playerOneMoveDown():
	playerMove(playerOne, False)

def playerTwoMoveDown():
	playerMove(playerTwo, False)


def getPlayerOneX():
	return playerOne.xcor()

def getPlayerOneY():
	return playerOne.ycor()




def getPlayerTwoX():
	return playerTwo.xcor()

def getPlayerTwoY():
	return playerTwo.ycor()


