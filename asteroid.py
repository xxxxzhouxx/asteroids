import pygame
import random
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            vector_one = self.velocity.rotate(random.uniform(20,50)) # return a new vector with random rotation at the reference of the original vector
            vector_two = self.velocity.rotate (- random.uniform(20,50))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = vector_one * 1.2
            asteroid_two.velocity = vector_two * 1.2
