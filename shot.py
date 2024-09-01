from pygame import Surface
from circleshape import *
from constants import *

class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)

	def update(self, dt: float):
		self.position += self.velocity * dt
	
	def draw(self, screen: Surface):
		pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
