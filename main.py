import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from logger import log_state
from circleshape import CircleShape
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt=0.0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip() #display updates on the screen
        dt = fps_clock.tick(60) / 1000 #limit to 60 fps and get delta time in seconds
        

if __name__ == "__main__":
    main()
