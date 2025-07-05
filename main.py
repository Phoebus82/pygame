from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import *
import pygame
import sys

def main():
	pygame.init
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock =pygame.time.Clock()
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	#asteroids
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	#asteroid filed
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
	#shoot
	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)
	#player
	Player.containers = (updatable, drawable)
	player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2), shots)

	dt = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for i in drawable:
			i.draw(screen)
		updatable.update(dt)
		for ast in asteroids:
			if ast.collision_check(player):
				print("Game over!")
				sys.exit()
			for shot in shots:
				if ast.collision_check(shot):
					ast.split()
				

		pygame.display.flip()
		clock.tick(60)
		dt = clock.tick(60) / 1000
		

if __name__ == "__main__":
	main()
	AsteroidField
