import pygame

class Star(pygame.sprite.Sprite):

    def __init__(self, name, classification, color_index, absolute_magnatiude,
    luminosity, surface_tempature, mass):
        super().__init__()
        
        self.name = name
        self.classification = classification
        self.color_index = color_index
        self.absolute_magnatiude = absolute_magnatiude
        self.luminosity = luminosity
        self.surface_tempature = surface_tempature
        self.mass = mass


