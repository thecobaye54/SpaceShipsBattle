import pygame

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, pos, speed, img):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pos
        self.speed = speed
        self.angle_speed = 5
        self.scale = 1.5
        
        self.rotation = 0

        self.image_origin = img

        self.image = img
        self.rect = self.image.get_rect()

    def update(self):
        self.image = pygame.transform.rotozoom(self.image_origin, self.rotation, self.scale)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def move(self, x_axis, y_axis):
        self.rotation -= x_axis*self.angle_speed

        vec = pygame.math.Vector2(0, 1)
        vec.y = y_axis*self.speed
        vec.rotate_ip(-self.rotation)

        self.pos = (self.pos[0] + vec.x, self.pos[1] + vec.y)
