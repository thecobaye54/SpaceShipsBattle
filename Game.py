import pygame
from pygame.locals import *

from SpaceShip import *


class Game:
    def __init__(self, res):
        self.res = res

        self.window_title = "SpaceShips Battle"
        self.is_running = True
        self.clock = pygame.time.Clock()

        self.player_ship_img = pygame.image.load("res/sprites/spaceship.png")
        self.player = SpaceShip((200, 200), 10, self.player_ship_img)

        self.start()

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.res)
        pygame.display.set_caption(self.window_title)

        self.run()

    def run(self):
        while self.is_running:
            for evt in pygame.event.get():
                self.manage_events(evt)
            self.manage_pressed_keys()
            self.update()
        self.quit()

    def manage_events(self, evt):
        if evt.type == QUIT:
            self.is_running = False
        # On va gérer d'autres évènements

    def manage_pressed_keys(self):
        pressed = pygame.key.get_pressed()

        vector = [0, 0]
        if pressed[K_q] or pressed[K_LEFT]:
            vector[0] -= 1
        if pressed[K_d] or pressed[K_RIGHT]:
            vector[0] += 1
        if pressed[K_z] or pressed[K_UP]:
            vector[1] -= 1
        if pressed[K_s] or pressed[K_DOWN]:
            vector[1] += 1
        
        self.player.move(vector[0], vector[1])

    def draw(self):
        self.screen.blit(self.player.image, self.player.rect)

    def update(self):
        self.screen.fill(50)

        self.player.update()
        self.draw()

        self.clock.tick(50)
        pygame.display.update()
    
    def quit(self):
        pygame.display.quit()
        pygame.quit()
        del self