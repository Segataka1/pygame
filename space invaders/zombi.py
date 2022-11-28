import pygame

class Zombi(pygame.sprite.Sprite):


    def __init__(self,screen) :
        super(Zombi, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/zombi.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = self.rect.x
        self.y = self.rect.y


    def draw(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        self.y += 0.1
        self.rect.y = self.y