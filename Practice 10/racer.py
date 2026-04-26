# Imports
import pygame
import sys
import random
import time
from pygame.locals import *

# Initialize pygame
pygame.init()
pygame.mixer.init()

# FPS settings
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
DARK_ROAD = (15, 15, 15)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 130, 0)
GRAY = (100, 100, 100)
LIGHT_GRAY = (180, 180, 180)

# Screen size
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Road settings
ROAD_LEFT = 50
ROAD_RIGHT = 350
ROAD_WIDTH = ROAD_RIGHT - ROAD_LEFT

# Object sizes
# Both cars have the same size
CAR_WIDTH = 45
CAR_HEIGHT = 80
COIN_SIZE = 32

# Game variables
SPEED = 5
MONEY_SCORE = 0
road_offset = 0

# Create game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Load images
icon = pygame.image.load("image/icon.png")
coin_icon = pygame.image.load("image/money.png")
coin_icon = pygame.transform.scale(coin_icon, (COIN_SIZE, COIN_SIZE))
pygame.display.set_icon(icon)

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)

# Load sounds
background_sound = pygame.mixer.Sound("sound/JENNIE_BLACKPINK_Tame_Impala_-_Dracula_Remix_(SkySound.cc).mp3")
crash_sound = pygame.mixer.Sound("sound/crash.wav")
coin_sound = pygame.mixer.Sound("sound/lost_money.wav")

# Play background sound in loop
background_sound.play(-1)


# Function for drawing moving road
def draw_road(surface, offset):
    # Draw green background around the road
    surface.fill(GREEN)

    # Draw gray road shoulders
    pygame.draw.rect(surface, GRAY, (ROAD_LEFT - 15, 0, ROAD_WIDTH + 30, SCREEN_HEIGHT))

    # Draw main black road
    pygame.draw.rect(surface, DARK_ROAD, (ROAD_LEFT, 0, ROAD_WIDTH, SCREEN_HEIGHT))

    # Draw white side border lines
    pygame.draw.line(surface, WHITE, (ROAD_LEFT, 0), (ROAD_LEFT, SCREEN_HEIGHT), 4)
    pygame.draw.line(surface, WHITE, (ROAD_RIGHT, 0), (ROAD_RIGHT, SCREEN_HEIGHT), 4)

    # Draw extra gray side details
    pygame.draw.line(surface, LIGHT_GRAY, (ROAD_LEFT - 10, 0), (ROAD_LEFT - 10, SCREEN_HEIGHT), 3)
    pygame.draw.line(surface, LIGHT_GRAY, (ROAD_RIGHT + 10, 0), (ROAD_RIGHT + 10, SCREEN_HEIGHT), 3)

    # Draw moving dashed center line
    line_width = 8
    line_height = 60
    gap = 80
    line_x = SCREEN_WIDTH // 2 - line_width // 2

    for y in range(-line_height, SCREEN_HEIGHT + gap, line_height + gap):
        pygame.draw.rect(
            surface,
            WHITE,
            (line_x, y + offset, line_width, line_height)
        )


# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load and resize coin image
        self.image = pygame.image.load("image/money.png")
        self.image = pygame.transform.scale(self.image, (COIN_SIZE, COIN_SIZE))
        self.rect = self.image.get_rect()

        # Coin appears randomly on the road
        self.rect.center = (random.randint(ROAD_LEFT + 30, ROAD_RIGHT - 30), 0)

    def move(self):
        # Move coin down
        self.rect.move_ip(0, SPEED)

        # If coin leaves the screen, return it to the top
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(ROAD_LEFT + 30, ROAD_RIGHT - 30), 0)


# Enemy car class
# Enemy car class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load enemy car image
        original_image = pygame.image.load("image/Enemy.png").convert_alpha()

        # Resize enemy without distortion
        new_width = 80
        old_width = original_image.get_width()
        old_height = original_image.get_height()
        new_height = int(old_height * new_width / old_width)

        self.image = pygame.transform.smoothscale(original_image, (new_width, new_height))
        self.rect = self.image.get_rect()

        # Enemy appears randomly on the road
        self.rect.center = (random.randint(ROAD_LEFT + 40, ROAD_RIGHT - 40), 0)

    def move(self):
        # Move enemy down
        self.rect.move_ip(0, SPEED)

        # If enemy leaves the screen, return it to the top
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(ROAD_LEFT + 40, ROAD_RIGHT - 40), 0)


# Player car class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load player car image
        original_image = pygame.image.load("image/Player.png").convert_alpha()

        # Resize player without distortion
        new_width = 80
        old_width = original_image.get_width()
        old_height = original_image.get_height()
        new_height = int(old_height * new_width / old_width)

        self.image = pygame.transform.smoothscale(original_image, (new_width, new_height))
        self.rect = self.image.get_rect()

        # Player starting position
        self.rect.center = (SCREEN_WIDTH // 2, 520)

    def move(self):
        # Get pressed keys
        pressed_keys = pygame.key.get_pressed()

        # Move left, but do not leave the road
        if self.rect.left > ROAD_LEFT:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        # Move right, but do not leave the road
        if self.rect.right < ROAD_RIGHT:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Create objects
P1 = Player()
E1 = Enemy()
M1 = Coin()

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)

money = pygame.sprite.Group()
money.add(M1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)


# Main game loop
while True:
    # Check all events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Move road lines
    road_offset += SPEED

    # Reset road animation offset
    if road_offset >= 140:
        road_offset = 0

    # Draw moving road instead of PNG background
    draw_road(DISPLAYSURF, road_offset)

    # Move and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Check collision between player and enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        background_sound.stop()
        crash_sound.play()

        time.sleep(0.5)

        # Show game over screen
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_text, (30, 250))
        pygame.display.update()

        # Remove all sprites
        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check collision between player and coin
    if pygame.sprite.spritecollideany(P1, money):
        coin_sound.play()

        # Increase coin score
        MONEY_SCORE += 1

        # Return coin to random top position
        M1.rect.top = 0
        M1.rect.center = (random.randint(ROAD_LEFT + 30, ROAD_RIGHT - 30), 0)

    # Show collected coins in the top right corner
    coin_text = font_small.render("Coins: " + str(MONEY_SCORE), True, YELLOW)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 130, 15))

    # Show coin icon near counter
    DISPLAYSURF.blit(coin_icon, (SCREEN_WIDTH - 170, 10))

    # Update display
    pygame.display.update()

    # Control FPS
    FramePerSec.tick(FPS)