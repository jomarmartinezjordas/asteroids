import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH )

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        split_angle = random.uniform(20,50)
        a1_movement = self.velocity.rotate(split_angle)
        a2_movement = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_two = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_one.velocity = a1_movement * 1.2
        asteroid_two.velocity = a2_movement * 1.2
