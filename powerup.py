import pygame
import random
from logger import log_event
from circleshape import CircleShape

class PowerUp(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw (self, screen):
        pass

    def update(self, dt: float):
        self.position += self.velocity * dt

