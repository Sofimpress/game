import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PLAYER_FILE_NAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.laser_sprites = []
        self.rect.centerx = SC_WIDTH//2
        self.rect.bottom = SC_HEIGHT - 20
        self.hp = PLAYER_MAX_HP
        self.speed = 0
        self.storona = 0
        self.fire_timer = pygame.time.get_ticks()




    def update(self):
        self.speedy = 0
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speedx = -8
            self.image = pygame.image.load(PLAYER_FILE_NAME2).convert_alpha()
        if keys[pygame.K_d]:
            self.speedx = 8
            self.image = pygame.image.load(PLAYER_FILE_NAME).convert_alpha()
        self.rect.x += self.speedx
        
        if self.rect.right > SC_WIDTH:
            self.rect.right = SC_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.fire()


        for laser in self.laser_sprites:
            laser.update()
            if laser.rect.bottom < 0:
                self.laser_sprites.remove(laser)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for laser in self.laser_sprites:
            screen.blit(laser.image, laser.rect)

    def fire(self):
        now = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()            
        if keys[pygame.K_SPACE] and now - self.fire_timer > FIRE_DELAY:
            self.fire_timer = now

            laser = Laser(self.rect.centerx, self.rect.top)
            self.laser_sprites.append(laser)

    def get_hp(self):
        return self.hp

    def reduce_hp(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def add_hp(self, hp):
        self.hp += hp
        if self.hp > 100:
            self.hp = 100
            
    def dis(self):
        if self.laser_sprites.rect.right <= 0 or laser_sprites.rect.left >= SC_WIDTH:
            self.laser_sprites.remove(laser) 
            
    def get_centerx(self):
        return self.rect.centerx

    def get_center(self):
        return self.rect.center

    def get_top(self):
        return self.rect.top

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(LASER_FILE_NAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = LASER_SPEEDY
        self.storona = 3
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.storona = 0
        if keys[pygame.K_d]:
            self.storona = 1
            
        if self.storona == 0:
            self.rect.x -= self.speedx
        if self.storona == 1:
            self.rect.x += self.speedx
            
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)





