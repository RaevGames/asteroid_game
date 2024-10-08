import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen: pygame.Surface):
		pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

	def update(self, dt: float):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius == ASTEROID_MIN_RADIUS:
			return
		rand_angle = random.uniform(20, 50)
		new_angle1 = self.velocity.rotate(rand_angle)
		new_angle2 = self.velocity.rotate(rand_angle * -1)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		new_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
		new_ast1.velocity = new_angle1 * 1.2
		new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
		new_ast2.velocity = new_angle2 * 1.2
