import pygame
import math

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLOCK_SIZE = 32
BOAT_SIZE = 44

class Boat:
    def __init__(self, x, y):
        self.position = [x, y]
        self.velocity = [0.0, 0.0]
        self.rotation = 0.0
        self.delta_rotation = 0.0
        self.inv_friction = 0.9
        self.water_level = y
        self.status = "IN_WATER"
        self.land_friction = 0.6

    def apply_gravity(self):
        if self.position[1] > self.water_level:
            self.velocity[1] -= 0.04  # Gravity effect
        else:
            self.velocity[1] = max(self.velocity[1], 0)  # Stop sinking

    def apply_friction(self):
        self.velocity[0] *= self.inv_friction
        self.velocity[1] *= self.inv_friction
        self.delta_rotation *= self.inv_friction

    def update_position(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.rotation += self.delta_rotation

    def control_boat(self, keys):
        if keys[pygame.K_LEFT]:
            self.delta_rotation -= 0.05
        if keys[pygame.K_RIGHT]:
            self.delta_rotation += 0.05
        if keys[pygame.K_UP]:
            self.velocity[0] += math.sin(math.radians(-self.rotation)) * 0.04
            self.velocity[1] += math.cos(math.radians(self.rotation)) * 0.04
        if keys[pygame.K_DOWN]:
            self.velocity[0] -= math.sin(math.radians(-self.rotation)) * 0.02
            self.velocity[1] -= math.cos(math.radians(self.rotation)) * 0.02

    def get_ground_friction(self):
        if self.status == "ON_LAND":
            return self.land_friction
        elif self.status == "IN_WATER":
            return 0.9
        elif self.status == "UNDER_WATER":
            return 0.45
        else:
            return 0.9

    def simulate_step(self, keys):
        self.apply_gravity()
        self.control_boat(keys)
        self.inv_friction = self.get_ground_friction()
        self.apply_friction()
        self.update_position()

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (*self.position, BOAT_SIZE, BOAT_SIZE))

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

boat = Boat(100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    boat.simulate_step(keys)

    screen.fill((255, 255, 255))
    boat.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()