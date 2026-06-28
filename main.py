import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from logger import log_state
from logger import log_event
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt=0.0
    updatable= pygame.sprite.Group()
    drawable= pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # place player in the center of the screen
    
    shots= pygame.sprite.Group()
    Shot.containers = (shots,updatable, drawable)

    asteroids= pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get(): # game keeps running until the user closes the window
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt) #change game state based on user input and time elapsed (movement, rotation, positions)

        for asteroid in asteroids: # check for collisions between the player and asteroids
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids: # check for collisions between shots and asteroids
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        for item in drawable: # renders the current state onto the screen (draws the player and other game objects)
            item.draw(screen)

        log_state() # log the current state of the game (positions, velocities, rotations, etc.) to a file for debugging or analysis
        pygame.display.flip() #display updates on the screen to be visible to the user
        dt = fps_clock.tick(60) / 1000 #limit to 60 fps and get delta time in seconds, which is used to make movement and rotation frame-rate independent

if __name__ == "__main__":
    main()
