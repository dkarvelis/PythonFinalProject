# Code for text_objects() gameOver() and Win() borrowed from https://pythonprogramming.net/pygame-python-3-part-1-intro/

import pygame
import time
import sys
from Colors import *
from Cars import *

# Game size window
width = 800
height = 600

lilyLanes = [200, 200, 200]
carLanes = [1000, 1000, 1000, 1000]

lilies0 = []
lilyMove0 = []
lilies1 = []
lilyMove1 = []
lilies2 = []
lilyMove2 = []

cars0 = []
cars1 = []
carMove1 = []
cars2 = []
carMove2 = []
cars3 = []

crashed = False

timer = 0

x = 400
y = 520

lives = 3

direction = 0

xMove = 0
yMove = 0

alive = True

#Putting "lilly pads" for player to jump to
def spawnLily(row):

	if row == 0:
		lilies0.append([800, 40])
		lilyMove0.append(0)
	elif row == 1:
		lilies1.append([-40, 80])
		lilyMove1.append(0)
	else:
		lilies2.append([800, 120])
		lilyMove2.append(0)
#Putting "car" like objects for player to avoid
def spawnCar(row):

	if row == 0:
		cars0.append([800, 320, getCarLeft()])
	elif row == 1:
		cars1.append([-40, 360, getCarRight()])
		carMove1.append(0)
	elif row == 2:
		cars2.append([800, 400, getCarLeft()])
		carMove2.append(0)
	else:
		cars3.append([-40, 440, getCarRight()])

def dispFrog(x, y, moved):
	gameDisplay.blit(pythons[moved], (x, y))

#Character movement
def keyPress(event):
	xChange = 0
	yChange = 0
	facing = 0
	if event.key == pygame.K_LEFT:
		xChange = -40
		facing = 1
	elif event.key == pygame.K_RIGHT:
		xChange = 40
		facing = 2
	elif event.key == pygame.K_UP:
		yChange = -40
		facing = 0
	elif event.key == pygame.K_DOWN:
		yChange = 40
		facing = 3
	return xChange, yChange, facing

# https://pythonprogramming.net/pygame-python-3-part-1-intro/
def text_objects(text, font, color="random"):
	textSurface = font.render(text, True, getColor(color))
	return textSurface, textSurface.get_rect()

# https://pythonprogramming.net/pygame-python-3-part-1-intro/
# Function for Game Over screen
def gameOver():
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects("Game Over", largeText)
	TextRect.center = ((width/2),(height/2 - 40))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(5)
# Function for the you win screen
def win():
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects("You Win!", largeText)
	TextRect.center = ((width/2),(height/2 - 40))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(5)
# Function for the bottom right timer
def gameClock(current):
	real = current // 60
	fake = real
	offset = 0
	while (fake//10) > 0:
		fake = fake // 10
		offset += 1
	largeText = pygame.font.Font('freesansbold.ttf', 20)
	TextSurf, TextRect = text_objects(str(real), largeText, "black")
	TextRect.center = ((790 - (offset * 5)),580)
	gameDisplay.blit(TextSurf, TextRect)

pygame.init()

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pythgger")

#Loading up images to be used for the objects in the game
lilyPad = pygame.image.load("ClyPad.png")

pythons = [pygame.image.load("PythggerUp.png"), pygame.image.load("PythggerLeft.png"),
		   pygame.image.load("PythggerRight.png"), pygame.image.load("PythggerDown.png"),
		   pygame.image.load("PythggerMini.png")]

clock = pygame.time.Clock()
# checking if game is running
while not crashed:

	alive = True
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		if event.type == pygame.KEYDOWN:
			xMove, yMove, direction = keyPress(event)

	x += xMove
	y += yMove
#logic for player snapping to lily pads
	xMove = 0
	yMove = 0

	if x < 0:
		x = 0
	elif x > width - 40:
		x = width - 40
	if not (y > 40 and y < 160):
		if(x % 40 != 0):
			diff = x % 40
			if diff <= 19:
				x -= diff
			else:
				x += 40 - diff
	if y > height - 80:
		y = height - 80
#Sets up play area
	gameDisplay.fill(getColor("green"))
	pygame.draw.rect(gameDisplay, getColor("dark"), [0, 320, 800, 160])
	pygame.draw.rect(gameDisplay, getColor("cyan"), [0, 0, 800, 40])
	pygame.draw.rect(gameDisplay, getColor("blue"), [0, 40, 800, 120])
	pygame.draw.rect(gameDisplay, getColor("white"), [0, 560, 800, 40])
	for val in range(lives):
		left = 40 * val + 10
		gameDisplay.blit(pythons[4], (left, 570))
	gameClock(timer)
#Logic for creating cars and liliypads and logic for their movement
	if(y == 120):
		alive = False
		for lily2 in lilies2:
			if(abs((lily2[0]+20) - (x + 20)) < 40):
				x = lily2[0]
				alive = True
	if(y == 80):
		alive = False
		for lily1 in lilies1:
			if(abs((lily1[0]+20) - (x + 20)) < 40):
				x = lily1[0]
				alive = True
	if(y == 40):
		alive = False
		for lily0 in lilies0:
			if(abs((lily0[0]+20) - (x + 20)) < 40):
				x = lily0[0]
				alive = True
	
	if(y == 320):
		for carCheck in cars0:
			if(abs((carCheck[0] + 20) - (x + 20)) < 41):
				alive = False
	if(y == 360):
		for carCheck in cars1:
			if(abs((carCheck[0] + 20) - (x + 20)) < 41):
				alive = False
	if(y == 400):
		for carCheck in cars2:
			if(abs((carCheck[0] + 20) - (x + 20)) < 41):
				alive = False
	if(y == 440):
		for carCheck in cars3:
			if(abs((carCheck[0] + 20) - (x + 20)) < 41):
				alive = False

	if(not alive):
		if(lives <= 1):
			lives -= 1
			pygame.draw.rect(gameDisplay, getColor("white"), [0, 560, 800, 40])
			for val in range(lives):
				left = 40 * val + 10
				gameDisplay.blit(pythons[4], (left, 570))
			gameClock(timer)
			gameOver()
			break
		else:
			x = 400
			y = 520
			direction = 0
			lives -= 1

	if lilyLanes[0] > 130:
		rando = random.randint(0, 300)
		if rando == 3:
			spawnLily(0)
			lilyLanes[0] = 0
	if lilyLanes[1] > 130:
		rando = random.randint(0, 300)
		if rando == 3:
			spawnLily(1)
			lilyLanes[1] = 0
	if lilyLanes[2] > 130:
		rando = random.randint(0, 300)
		if rando == 3:
			spawnLily(2)
			lilyLanes[2] = 0

	if carLanes[0] > 200:
		rando = random.randint(0, 5)
		if rando == 3:
			spawnCar(0)
			carLanes[0] = 0
	if carLanes[1] > 300:
		rando = random.randint(0, 150)
		if rando == 3:
			spawnCar(1)
			carLanes[1] = 0
	if carLanes[2] > 200:
		rando = random.randint(0, 20)
		if rando == 3:
			spawnCar(2)
			carLanes[2] = 0
	if carLanes[3] > 200:
		rando = random.randint(0, 10)
		if rando == 3:
			spawnCar(3)
			carLanes[3] = 0

	lilyLanes[0] += 1
	lilyLanes[1] += 1
	lilyLanes[2] += 1
	
	carLanes[0] += 1
	carLanes[1] += 1
	carLanes[2] += 1
	carLanes[3] += 1


	for index, lily in enumerate(lilies0):
		gameDisplay.blit(lilyPad, tuple(lily))
		if(lilyMove0[index] == 1):
			lily[0] -= 1
			lilyMove0[index] = 0
		else:
			lilyMove0[index] += 1

	for index, lily in enumerate(lilies1):
		gameDisplay.blit(lilyPad, tuple(lily))
		if(lilyMove1[index] == 3):
			lily[0] += 2
			lilyMove1[index] = 0
		else:
			lilyMove1[index] += 1

	for index, lily in enumerate(lilies2):
		gameDisplay.blit(lilyPad, tuple(lily))
		if(lilyMove2[index] == 2):
			lily[0] -= 1
			lilyMove2[index] = 0
		else:
			lilyMove2[index] += 1

	for index, car in enumerate(cars0):
		gameDisplay.blit(pygame.image.load(car[2]), (car[0], car[1]))
		car[0] -= 2

	for index, car in enumerate(cars1):
		gameDisplay.blit(pygame.image.load(car[2]), (car[0], car[1]))
		if(carMove1[index] == 1):
			car[0] += 1
			carMove1[index] = 0
		else:
			carMove1[index] += 1

	for index, car in enumerate(cars2):
		gameDisplay.blit(pygame.image.load(car[2]), (car[0], car[1]))
		if(carMove2[index] == 1):
			car[0] -= 2
			carMove2[index] = 0
		else:
			carMove2[index] += 1

	for index, car in enumerate(cars3):
		gameDisplay.blit(pygame.image.load(car[2]), (car[0], car[1]))
		car[0] += 1

	if len(lilies0) > 0 and lilies0[0][0] < -40:
		lilies0 = lilies0[1:]
		lilyMove0 = lilyMove0[1:]
	if len(lilies1) > 0 and lilies1[0][0] > 800:
		lilies1 = lilies1[1:]
		lilyMove1 = lilyMove1[1:]
	if len(lilies2) > 0 and lilies2[0][0] < -40:
		lilies2 = lilies2[1:]
		lilyMove2 = lilyMove2[1:]

	if len(cars0) > 0 and cars0[0][0] < -40:
		cars0 = cars0[1:]
	if len(cars1) > 0 and cars1[0][0] > 800:
		cars1 = cars1[1:]
		carMove1 = carMove1[1:]
	if len(cars2) > 0 and cars2[0][0] < -40:
		cars2 = cars2[1:]
		carMove2 = carMove2[1:]
	if len(cars3) > 0 and cars3[0][0] > 800:
		cars3 = cars3[1:]
#Timer and updating display also checks for Winning condition
	timer += 1
	dispFrog(x, y, direction)
	if y < 40:
		win()
		break
	print(event)
	pygame.display.update()
	clock.tick(60)

pygame.quit()

print("Thanks for playing! :)")