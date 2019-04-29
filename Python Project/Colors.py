import random

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
gray = (128, 128, 128)
dark = (60, 60, 60)
light = (200, 200, 200)
randomColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

backgroundColors = {"red" : red, "green" : green, "blue" : blue,
					"black" : black, "white" : white, "yellow" : yellow, 
					"magenta" : magenta, "cyan" : cyan, "gray" : gray, 
					"dark" : dark, "light" : light, "random" :randomColor}

def getColor(index):
	return backgroundColors[index]
