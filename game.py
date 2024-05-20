import pygame
import sys
from settings import *
from player import Player
from player import Laser
from meteor_manager import MeteorManager
from text_obj import Text_Obj

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.player = Player()
        self.meteor_manager = MeteorManager()
        self.score = 0
        self.text_score = Text_Obj(10, 10, self.score)
        self.text_hp = Text_Obj(500, 10, self.player.get_hp())

    def play(self):
        while self.run:
            self.check_events()
            self.update()
            self.check_collisions()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def check_events(self):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.player.update()
        self.meteor_manager.update()
        self.text_hp.update(self.player.get_hp())
        self.text_score.update(self.score)

    def check_collisions(self):
        for meteor in self.meteor_manager.meteors:
            if self.player.rect.colliderect(meteor.rect):
                self.player.reduce_hp(meteor.get_damage())
                meteor.random_position()
        for laser in self.player.laser_sprites:
            if laser.rect.centerx <= 0 or laser.rect.centerx >= SC_WIDTH:
                self.player.laser_sprites.remove(laser)
        for meteor in self.meteor_manager.meteors:
            for laser in self.player.laser_sprites:
                if meteor.rect.colliderect(laser.rect):
                    #self.bonus_manager.generate_bonus(meteor)
                    #self.explosion_manager.generate_explosion(meteor)
                    meteor.random_position()
                    self.player.laser_sprites.remove(laser)
                    self.score += meteor.get_score()

    def draw(self):
        self.screen.fill(BLACK)
        self.player.draw(self.screen)
        self.meteor_manager.draw(self.screen)
        self.text_hp.draw(self.screen)
        self.text_score.draw(self.screen)
        pygame.display.update()

    def game_over(self):
        while True:
            self.check_events()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.run = False
                break
            self.screen.fill(BLACK)
            self.game_over_bg.draw(self.screen)
            pygame.display.update()

