import pygame

# Variables

origin_x = 127
origin_y = 830
posX_sf = 813/960
posY_sf = 830/980

class Star(pygame.sprite.Sprite):

    """
    posx and posy are temporarily included for testing. Future versions
    will have the x and y positions calculated from tempature and 
    luminonsity values
    """
    def __init__(self, name, classification, color_index, absolute_magnatiude,
    luminosity, surface_tempature, mass, posx, posy):
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
        self.posx = origin_x + (posx * posX_sf)
        self.posy = origin_y - (posy * posY_sf)
        
    def display(self, surface, color):
        pygame.draw.circle(surface, color, (self.posx, self.posy), 10)
