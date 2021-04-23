import pygame
from star import Star

# Initialize game engine
pygame.init()

# Images
base_image = pygame.image.load("assets/base_diagram.jpg")

# Stages
START = 0
PLAYING = 1
END = 2
PAUSE = 3

# Program Variables
done = False
stage = START

# Window
WIDTH = 960
HEIGHT = 980

# Diagram Dimensions 
# X-axis 127-940
# Y-axis 18-830

SIZE = (WIDTH, HEIGHT)
TITLE = "Hertspring Russel Diagram"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60
display_clock = 0

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (100, 255, 100)
SKYBLUE = (0, 238, 255)

# Star List
star_list = [
   Star("Betelgeuse", "M2", 2.06, -5.85, 150000, 3500, 20),
   Star("Antares", "M1", 1.83, -5.28, 1.6, 18500, 7.2),
   Star("Proxima Centauri", "M5.5", 1.82, 11.05, .0017, 3042, .123)
]

def setup():
    global visible_stars
    # Sets initial state of the program
    stage == START

# Program loop
setup()

while not done:
    # Input handling (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game Logic (Preforms ingame actions and controls the program.)
     
    # Drawing Logic (Draws the graphics and sprites on screen)
    screen.blit(base_image, [0,0])

    # Displays each instance of Star in star_list
    for star in star_list:
        star.display(screen, WHITE)

        print(star.posx, star.posy)

    # Update screen (Draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()

