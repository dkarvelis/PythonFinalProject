import random

carsRight = ["JavaRight.png", 
			 "RubyRight.png",
			 "SwiftRight.png"]

carsLeft = ["JavaLeft.png",
			"RubyLeft.png",
			"SwiftLeft.png"]

def getCarRight():
	return carsRight[random.randint(0, len(carsRight) - 1)]

def getCarLeft():
	return carsLeft[random.randint(0, len(carsLeft) - 1)]