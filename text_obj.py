import pygame
from settings import *

class Text_Obj:

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.font = pygame.font.SysFont('arial', 32)
        

    def update(self, value):
        self.value = value
        self.text = self.font.render(str(self.value), True, WHITE)
        self.text_rect = self.text.get_rect()
        self.text_rect = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
