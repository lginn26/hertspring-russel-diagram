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

    def display(self, surface, color):
        radius = (temp_size_sf * self.posx) + ((lum_size_sf * (1192 - self.posy)))
        pygame.draw.circle(surface, color, (self.posx, self.posy), radius)
