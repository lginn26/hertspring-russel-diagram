import math
import pygame
from star import Star

# Initialize game engine
pygame.init()

# Images
base_image = pygame.image.load("assets/base_diagram.jpg")

# Fonts
font1 = pygame.font.Font("assets/SpaceGrotesk-VariableFont_wght.ttf", 20)

# Stages
START = 0
PLAYING = 1
END = 2
PAUSE = 3

# Program Variables
done = False
stage = START

# Window
WIDTH = 1300
HEIGHT = 1000

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

# Functions
def display_message(message):
    star_txt = font1.render(message, 1, RED)
    w = star_txt.get_width()
    screen.blit(star_txt, [0, 950])

# Star List
star_list = [
   Star("The Sun",	"G2V",0.63,4.83,1,5700,1),
   Star("Achernar",	"B3V",	-0.16,	-2.77,	3150,15000,6.7),
   Star("Acrux","B1V",-0.26,-3.77,25000,24000,15.52),
   Star("Adhara",	"B2 II",-0.21,-4.8,38700,22900,12.6),
   Star("Aldebaran",	"K5+ III",	1.44,	-2.1,	518,	3910,	1.7),
   Star("Alpha Centauri",	"G2V",	0.71,	4.38,	1.519,	5790,	1.1),
   Star("Altair",	"A7 V",	0.09,	2.22,	10.6,	7700,	1.79),
   Star("Antares",	"M1",	1.83,	-5.28,	1.6,	18500,	7.2),
   Star("Arcturus",	"K0 III",	1.23,	-0.04,	170,	4290,	1.1),
   Star("Barnard's Star",	"M4",	1.713,	9.511,	0.0004,	3134,	144),
   Star("Betelgeuse",	"M2",	2.06,	-5.85,	150000,	3500,	20),
   Star("Canopus",	"A9 II",	0.1,	-5.71,	107000,	7400,	9.8),
   Star("Capella",	"G3 III",	0.44,	0.08,	77.6,	4940,	2.69),
   Star("Castor",	"A1V",	0.03,	0.986,	34,	10286,	2.76),
   Star("Deneb",	"A2",	0.23,	-8.38,	196000,	8525,	19),
   Star("Formalhaut",	"A3V",	0.08,	1.72,	16.63,	8590,	1.92),
   Star("Gacrux",	"M3",	1.59,	-0.52,	820,	3626,	1.3),
   Star("Hadar",	"B1VIII",	-0.23,	-5.42,	41700,	25500,	4.61),
   Star("Pollux",	"K0III",	1,	1.07,	43,	4865,	2.04),
   Star("Polaris",	"F7Ib",	0.01,	-3.62,	1260,	6015,	6.5),
   Star("Procyon B",	"DQZ",	0.42,	10.7,	0.00055,	7740,	0.602),
   Star("Proxima Centauri",	"M5.5",	1.82,	11.05,	0.0017,	3042,	0.123),
   Star("Regulus",	"B7V",	-0.11,	-0.52,	316.2,	12460,	3.5),
   Star("Rigel",	"B8Ia",	-0.06,	-6.72,	66000,	11000,	17),
   Star("Shaula",	"B2IV",	-0.240,	-5.05,	36300,	25000,	11),
   Star("Sirius",	"A1",	-0.03,	-1.46,	25.4,	9940,	2.02),
   Star("Spica",	"B1",	-0.23,	-3.55,	12100,	22399,	10.3),
   Star("Van Maanen's Star",	"DZ8",	0.546,	12.374,	0.00016,	6220,	0.633),
   Star("Vega",	"A0",	0,	0.03,	50,	9602,	2.135),
   Star("Wolf 359",	"M6",	2.034,	13.54,	0.0014,	2800,	0.09)

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
    displayed_star = None

    message = "Hover close to the center of a star to reveal its data!"
    for star in star_list:
        star.display(screen)

        distx = abs(pygame.mouse.get_pos()[0] - star.posx)
        disty = abs(pygame.mouse.get_pos()[1] - star.posy)
        distance = math.sqrt( math.pow(distx, 2) +  math.pow(disty, 2))

        if (distance < star.radius):
            message = "{}: class:{}, color index:{}, absolute magnitude:{}, luminosity:{} SL, surface tempature:{} K, mass:{} SM".format(star.name, star.classification, star.color_index, star.absolute_magnatiude, star.luminosity, star.surface_tempature, star.mass)

    display_message(message) 

    # Update screen (Draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()

