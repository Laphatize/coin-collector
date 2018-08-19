# pgzrun /Users/Ramesh/Desktop/Pranav/Python-Projects/coin-collector/coin.py 


from random import randint


DEVELOPERMODE = True #  Set this to True to see important details logged to console.


WIDTH = 400 # do not change, sets size of windows

HEIGHT = 400 # ^


score = 0 # < change that if ya want, don't see why. 

game_over = False # prevents the gameover screen from showing at start

# Fox image, and initial position
fox = Actor("fox")
fox.pos = 100, 100

# Get coin image, and initial position
coin = Actor("coin") 
coin.pos = 200, 200
 
# TO-DO
# spike = Actor("spike")
# spike.pos = 200, 200
#
#
# def place_spike():
#	spike.x = randint(20, (WIDTH - 20))
#	spike.y = randint(20, (HEIGHT - 20))



#	if DEVELOPERMODE:
#		print(spike.x)
#		print(spike.y)


def draw():

	# Set's main gamespace
	screen.fill("lightgreen") 
	fox.draw() 
	coin.draw()
#	spike.draw()
	screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))
	screen.draw.text("Laphatize Creations", color="black", topleft=(10,30))

	# Game Over Screeb
	if game_over:
		
		screen.fill("pink") # Change background to pink.

		screen.draw.text("Times Up! :( ", topleft=(10,60), fontsize=60) 

		screen.draw.text("Final Score: " + str(score), color="black", topleft=(10,10), fontsize=60) 
		
		screen.draw.text("R.I.P Fox 2018.", topleft=(10,1))



def place_coin():
	coin.x = randint(20, (WIDTH - 20))
	coin.y = randint(20, (HEIGHT - 20))

def time_up():
	global game_over
	game_over = True
	place_coin()





def update():
	global score

	speed = 5


	if keyboard.left:
		fox.x = fox.x - speed
		fox.image = "foxleft"

	if keyboard.right:
		fox.x = fox.x + speed
		fox.image = "fox"


	if keyboard.up:
		fox.y = fox.y - speed

	if keyboard.down:
		fox.y = fox.y + speed

	coin_collected = fox.colliderect(coin)

	if coin_collected:
		score = score + 10
		place_coin()
		sounds.piccoin.play()
#		place_spike()
		speed = speed - .2

#	spike_touched = fox.colliderect(spike)

#	if spike_touched:
#		game_over = True




clock.schedule(time_up, 16.0)
place_coin()