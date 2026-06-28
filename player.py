import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOT_SPEED
from constants import PLAYER_SHOT_COOLDOWN_SECONDS
from shot import Shot
from shot import SHOT_RADIUS

class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.PLAYER_SHOT_COOLDOWN_TIMER = 0

        # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate (self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.PLAYER_SHOT_COOLDOWN_TIMER <= 0:
                self.PLAYER_SHOT_COOLDOWN_TIMER = PLAYER_SHOT_COOLDOWN_SECONDS
                self.shoot()
            self.PLAYER_SHOT_COOLDOWN_TIMER -= dt

    def move (self,dt):
        unit_vector=pygame.Vector2(0,1)
        rotated_vector=unit_vector.rotate(self.rotation)
        self.position += rotated_vector * PLAYER_SPEED * dt
    
    def shoot(self):
        shot=Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

    

