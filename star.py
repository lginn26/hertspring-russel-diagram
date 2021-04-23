import pygame
import math

# Variables

origin_x = 127
origin_y = 479
posX_sf = 813/35000
#posY_sf = 

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
        self.posx = origin_x + ( 813 - (surface_tempature * posX_sf))
        self.posy = origin_y - (math.log(luminosity, 10) * 70)
        
    def display(self, surface, color):
        pygame.draw.circle(surface, color, (self.posx, self.posy), 10)
