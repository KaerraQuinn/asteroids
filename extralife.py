import pygame
from logger import log_event
from powerup import PowerUp
from constants import LINE_WIDTH

class ExtraLife(PowerUp):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, LINE_WIDTH)

