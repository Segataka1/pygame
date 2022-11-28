import pygame, sys
from bullet import Bullet
from zombi import Zombi
import time

def events(screen, gun, bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color,screen,stats, score, gun, zombies, bullets):
        screen.fill(bg_color)
        score.show_score()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        gun.output()
        zombies.draw(screen)
        pygame.display.flip()


def update_bullets(screen, stats, score, zombies, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, zombies, True, True)
    if collisions:
        for zombies in collisions.values():
            stats.score += 10 * len(zombies)
        score.image_score()
        check_high_score(stats, score)
        score.image_guns()
    if len(zombies) == 0:
        bullets.empty()
        create_army(screen, zombies)


def gun_kill(stats, screen, score, gun, zombies, bullets):
    if stats.guns_left > 0:
        stats.guns_left -= 1
        score.image_guns()
        zombies.empty()
        bullets.empty()
        create_army(screen, zombies)
        gun.create_gun()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()


def update_zombies(stats, screen,score, gun, zombies, bullets):
    zombies.update()
    if pygame.sprite.spritecollideany(gun, zombies):
        gun_kill(stats, screen,score, gun,zombies, bullets)
    zombies_check(stats, screen,score, gun,zombies, bullets)


def zombies_check(stats, screen,score, gun, zombies, bullets):
    screen_rect = screen.get_rect()
    for zombi in zombies.sprites():
        if zombi.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, score, gun, zombies, bullets)
            break

def create_army(screen, zombies):
    zombi = Zombi(screen)
    zombi_width = zombi.rect.width
    number_zombi_x = int ((700 - 2 * zombi_width) / zombi_width)
    zombi_height = zombi.rect.height
    number_zombi_y = int((800 - 100 - 2 * zombi_height) / zombi_height)


    for row_number in range(number_zombi_y - 1):
        for zombi_number in range(number_zombi_x):
            zombi = Zombi(screen)
            zombi.x = zombi_width + (zombi_width * zombi_number)
            zombi.y = zombi_height + (zombi_height * row_number)
            zombi.rect.x = zombi.x
            zombi.rect.y = zombi.rect.height + (zombi.rect.height * row_number)
            zombies.add(zombi)  

def check_high_score(stats, score):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.image_high_score()
        with open ('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
