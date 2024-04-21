import pygame 
import sys
from player_anim import Player
from rain import Rain

clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meadow")

background = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\поляна1.png'),(WIDTH, HEIGHT))


star = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\звезда.png'),(80, 80))
star_dark = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\звездат.png'),(80, 80))


def Meadow():
    x = 0
    y = 400
    speed = 10
    player = Player(x, y, speed)

    running = True
    while running:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                MENU_MOUSE_POS = pygame.Rect(mouse_x, mouse_y, 1, 1)
                if invisible_star_rect.colliderect(MENU_MOUSE_POS):
                    Rain()

        screen.fill((0,0,0))
        screen.blit(background,(0, 0))
        invisible_star_rect = pygame.Rect(30, 450, 20, 20)
        screen.blit(star, (10,425))
        #pygame.draw.rect(screen, (255,255,255), invisible_star_rect)

        if player.player_rect.colliderect(invisible_star_rect):
            screen.blit(star_dark,(10, 425))

        player.update()
        player.draw(screen)


        pygame.display.flip()
        clock.tick(30)