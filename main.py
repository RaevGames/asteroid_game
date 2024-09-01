import pygame
from asteroidfield import AsteroidField
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	# Groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		# Update
		item: CircleShape
		asteroid: Asteroid
		shot: Shot
		for item in updatable:
			item.update(dt)
		# Collision
		for asteroid in asteroids:
			if asteroid.is_colliding(player):
				print("Game over!")
				exit()
			for shot in shots:
				if asteroid.is_colliding(shot):
					asteroid.split()
					shot.kill()
		# Rendering
		screen.fill((0,0,0))
		for item in drawable:
			item.draw(screen)
		pygame.display.flip()
		# Post-Render
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()