# pgzrun /Users/Ramesh/Desktop/Pranav/Python-Projects/coin-collector/coin.py 
# laphatize


from random import randint

WIDTH = 400 # do not change, sets size of windows

HEIGHT = 400 # ^

score = 0 # < change that if ya want, don't see why. 

game_over = False # prevents the gameover screen from showing at start

# fox image, and initial position
fox = Actor("fox")
fox.pos = 100, 100

# get coin image, and initial position
coin = Actor("coin") 
coin.pos = 200, 200

def draw():

	# the screen you see when you play
	screen.fill("green") # background (Grass)
	fox.draw() # the fox, thanks random person who made it
	coin.draw() # the coin
	screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))
	screen.draw.text("Laphatize Creations", color="black", topleft=(10,30))

	# game over screen, rip
	if game_over:
		screen.fill("pink")
		screen.draw.text("Final Score: " + str(score), color="black", topleft=(10,10), fontsize=60)

def place_coin():
	coin.x = randint(20, (WIDTH - 20))
	coin.y = randint(20, (HEIGHT - 20))

def time_up():
	global game_over
	game_over = True
	clock.schedule(time_up, 7.0)
	place_coin()

def update():
	global score


	if keyboard.left:
		fox.x = fox.x - 2

	if keyboard.right:
		fox.x = fox.x + 2



	if keyboard.up:
		fox.y = fox.y - 2

	if keyboard.down:
		fox.y = fox.y + 2

	coin_collected = fox.colliderect(coin)

	if coin_collected:
		score = score + 10
		place_coin()





place_coin()