import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        
        new_angles = random.uniform(20, 50)
        dir1 = self.velocity.rotate(new_angles) * 1.2
        dir2 = self.velocity.rotate(-new_angles) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        return [
            (self.position.x, self.position.y, new_radius, dir1),
            (self.position.x, self.position.y, new_radius, dir2)
        ]