import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
import player
from circleshape import CircleShape
import asteroid
import asteroidfield
import sys
import shot

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)

    new_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)

    shots = pygame.sprite.Group()
    shot.Shot.containers = (shots, updatable, drawable)

    asteroidfield.AsteroidField.containers = (updatable)
    asteroid_field = asteroidfield.AsteroidField()



    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid_ind in asteroids:
            if new_player.collides_with(asteroid_ind) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid_ind in asteroids:
            for shot_ind in shots:
                if shot_ind.collides_with(asteroid_ind) == True:
                    log_event("asteroid_shot")
                    pygame.sprite.Sprite.kill(shot_ind)
                    asteroid_ind.split()

        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        # new_player.draw(screen)
        pygame.display.flip()



        dt = clock.tick(60) / 1000


        # print(dt)


if __name__ == "__main__":
    main()
