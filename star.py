import pygame
import math

# Diagram Dimensions
# X-Axis Length: 1192
# Y-Axis Length: 860

# X-Step: 100
# Y-Step: 75

# X-Origin: 1280
# Y-Origin: 530 

# Variables

origin_x = 1280
origin_y = 530

x_step = 100
y_step = 75

temp_step = 3000
lum_step = 0

temp_size_sf = 20/1192
lum_size_sf = 20/860

color_scheme_barrier = 10000

class Star(pygame.sprite.Sprite):

    """
    posx and posy are temporarily included for testing. Future versions
    will have the x and y positions calculated from tempature and 
    luminonsity values
    """
    def __init__(self, name, classification, color_index, absolute_magnatiude,
    luminosity, surface_tempature, mass):
        super().__init__()
        
        # Star Data
        self.name = name
        self.classification = classification
        self.color_index = color_index
        self.absolute_magnatiude = absolute_magnatiude
        self.luminosity = luminosity
        self.surface_tempature = surface_tempature
        self.mass = mass

        # Object Data
        self.posx = origin_x - (x_step * (surface_tempature / temp_step))
        self.posy = origin_y - (math.log10(luminosity) * y_step)
        self.radius = (temp_size_sf * self.posx) + ((lum_size_sf * (1192 - self.posy)))

    def display(self, surface):

        # Calculate Color
        star_type = self.classification[0:1]
        if (star_type == "O"):
            color = [0, 110, 255]
            color2 = [0, 90, 235]
        elif (star_type == "B"):
            color = [99, 167, 255]
            color2 = [79, 80, 225]
        elif (star_type == "A" or star_type == "F"):
            color = [255, 255, 255]
            color2 = [235, 235, 235]
        elif (star_type == "G"):
            color = [255, 255, 0]
            color2 = [235, 235, 0]
        elif (star_type == "K"):
            color = [255, 136, 0]
            color2 = [235, 116, 0]
        else:
            color = [255, 0, 0]
            color2 = [235, 0, 0]

        # Draw Star
        pygame.draw.circle(surface, color2, (self.posx, self.posy), self.radius)
        pygame.draw.circle(surface, color, (self.posx, self.posy), self.radius-2)
