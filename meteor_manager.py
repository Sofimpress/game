import pygame
from settings import *
from meteor import Meteor
from random import randint

class MeteorManager:
    def __init__(self):
        filename_list = ["big_zmea1.jpg", "lit_zmea1.jpg"]
        filename_list2 = ["big_zmea2.jpg", "lit_zmea2.jpg"]
        
        self.meteors = []
        for filename in filename_list:
            meteor = Meteor("images\\" + filename)
            meteor.random_position()
            if filename.find("big") > 0:
                meteor.set_damage(50)
                meteor.set_score(5)
            elif filename.find("lit") > 0:
                meteor.set_damage(30)
                meteor.set_score(15)
            #elif filename.find("2") > 0:
                #meteor.set_speedx(-2)
                #meteor.rect.x = 800
                #meteor.rect.x = 10  
            #elif filename.find("1") > 0:
                #meteor.set_speedx(2)
                #meteor.rect.x = 0
                #meteor.rect.y = 10  

    def update(self):
        for meteor in self.meteors:
            meteor.update()
            if meteor.rect.right <= 0 or meteor.rect.left >= SC_WIDTH \
            or meteor.rect.top >= SC_HEIGHT:
                meteor.random_position()

    def draw(self, screen):
        for meteor in self.meteors:
            meteor.draw(screen)
