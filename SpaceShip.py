import pygame
import time

from Bullet import *

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, pos, speed, img, bullet_img):
        pygame.sprite.Sprite.__init__(self)

        self.bullet_img = bullet_img
        self.bullet_timer = 0.2
        self.start_time = 0
        self.can_fire = True

        self.pos = pos
        self.speed = speed
        self.angle_speed = 5
        self.scale = 1.5
        
        self.rotation = 0
        self.direction = pygame.math.Vector2(0, 1)

        self.image_origin = img

        self.image = img
        self.rect = self.image.get_rect()

    def update(self):
        self.image = pygame.transform.rotozoom(self.image_origin, self.rotation, self.scale)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        if time.time() - self.start_time >= self.bullet_timer:
            self.can_fire = True

    def move(self, x_axis, y_axis):
        delta_rot = x_axis*self.angle_speed
        self.rotation -= delta_rot

        vec = pygame.math.Vector2(0, 1)
        vec.y = y_axis*self.speed
        vec.rotate_ip(-self.rotation)

        self.direction.rotate_ip(delta_rot)
        self.direction.normalize_ip()

        self.pos = (self.pos[0] + vec.x, self.pos[1] + vec.y)

    def fire(self):
        if self.can_fire:
            self.can_fire = False
            self.start_time = time.time()
            return Bullet(self.pos, (self.direction.x, self.direction.y), 15, self.bullet_img)