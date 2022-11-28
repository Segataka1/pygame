import pygame, control
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from score import Score
 

def run(): 

    pygame.init()
    screen = pygame.display.set_mode((700,800))
    pygame.display.set_caption("space invaders (test)")
    bg_color = (0,0,0) 
    gun = Gun(screen)  
    bullets = Group()
    zombies = Group() 
    control.create_army(screen, zombies)
    stats = Stats() 

    score = Score(screen,stats)


    while True:
        control.events(screen,gun, bullets)
        if stats.run_game:
            gun.update_gun()
            control.update(bg_color,screen,stats, score, gun, zombies, bullets)
            control.update_bullets(screen,stats, score, zombies, bullets)
            control.update_zombies(stats, screen,score, gun, zombies, bullets)

run()
