import pygame
import sys
import time
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state, log_event
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    Shot.containers = (shots, drawable, updatable)
    Score = 0
    Lives = 3
    IMMUNITY_END = pygame.USEREVENT + 1
    while True:
        log_state()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == IMMUNITY_END:
                player.immune = False
            if event.type == pygame.QUIT:
                return
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                return
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                collision = asteroid.collides_with(shot)
                if collision:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    log_event("Score")
                    Score += 10
            collision = asteroid.collides_with(player)
            if collision:
                if player.immune is False:
                    if Lives <= 0:
                        log_event("player_hit")
                        print (f"Game Over!")
                        print (f"SCORE:{Score}")
                        sys.exit()
                    else:
                        log_event("player_hit")
                        Lives -= 1
                        player.immune = True
                        pygame.time.set_timer(IMMUNITY_END, 500)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
