from util import *
import turtle

scoreOfOne = 0
scoreOfTwo = 0


scorer = turtle.Turtle()
createObject(scorer)
scorer.hideturtle()
scorer.goto(0, 350)



def getScoreOne():
	return scoreOfOne

def getScoreTwo():
	return scoreOfTwo

def clear():
	scorer.clear()


def writeScore(one, two):
	scorer.write("Player A: {} | Player B: {}".format(one, two), align="center", font=("Courier", 24, "normal"))


writeScore(scoreOfOne, scoreOfTwo)


def increaseScoreOfOne():
	global scoreOfOne
	scoreOfOne += 1



def increaseScoreOfTwo():
	global scoreOfTwo
	scoreOfTwo += 1


