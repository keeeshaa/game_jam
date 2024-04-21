import pygame 
import sys
from player_anim import Player
import random
from maze_main import maze
from counter import Counter

clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tree")

background = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\tree.jpeg'),(WIDTH, HEIGHT))

atmo = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\light.png')

star = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\звезда.png'),(80, 80))
star_dark = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\звездат.png'),(80, 80))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("minecraft.otf", size)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)



class MovingImage:
    def __init__(self):
        self.x = random.randint(-30, WIDTH - 30)
        self.y = random.randint(-30, HEIGHT - 30)
        self.speed_x = random.randint(1, 2) or random.randint(-1, 0)  # Случайная скорость по оси X
        self.speed_y = random.randint(-1, 0) or random.randint(1, 2) # Случайная скорость по оси Y

    def update(self):
        # Движение изображения
        self.x += self.speed_x
        self.y += self.speed_y


    def draw(self):
        screen.blit(atmo, (self.x, self.y))


objects = []


def Tree():
    x = 800
    y = 450
    speed = 10
    player = Player(x, y, speed)

    running = True
    while running:
        #counter = Counter()
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                MENU_MOUSE_POS = pygame.Rect(mouse_x, mouse_y, 1, 1)
                if invisible_star_rect.colliderect(MENU_MOUSE_POS):
                    maze()

        screen.fill((0,0,0))
        screen.blit(background,(0, 0))
        invisible_star_rect = pygame.Rect(30, 450, 20, 20)
        screen.blit(star, (10,425))
        #pygame.draw.rect(screen, (255,255,255), invisible_star_rect)

        #elapsed_time = counter.get_elapsed_time() // 1000  # Преобразование времени в секунды
        #draw_text(f"Time: {elapsed_time}s", get_font(30), (255, 255, 255), screen, 50, 50)

        if player.player_rect.colliderect(invisible_star_rect):
            screen.blit(star_dark,(10, 425))

        player.update()
        player.draw(screen)

        if random.random() < 0.012:
            new_object = MovingImage()
            objects.append(new_object)
        for obj in objects:
            obj.update()
            obj.draw()
        
        pygame.display.flip()
        clock.tick(30)


