import pygame
from logger import log_event
from powerup import PowerUp
from player import Player
from constants import LINE_WIDTH

class Shield(PowerUp):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, LINE_WIDTH)

    def draw_bubble(self):
        shield_bubble = True
        if shield_bubble:
            pygame.draw.circle(screen, "blue", self.position, self.radius, LINE_WIDTH)
