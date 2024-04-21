import pygame
import sys
from player_umb import Player_Umbrella
#from counter import Counter
import main as main

pygame.init()

x = 400
y = 400
speed = 10

invisible_eng_rect = pygame.Rect(240, 500, 50, 175)
invisible_umb_rect = pygame.Rect(700, 600, 25, 50)
invisible_back_rect = pygame.Rect(500,250,50,50)

took_umbrella = False

clock = pygame.time.Clock()
WIDTH = 1000
HEIGHT= 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Den")

umb = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\лист.png'),(400,400))
umb_light = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\листсвет.png'),(400,400))

pers = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\player.png')
pers = pygame.transform.scale(pers, (200, 200))

background = pygame.transform.scale(pygame.image.load(r"C:\Users\Admin\Desktop\pp2\main\images\пещера.png"),(WIDTH, HEIGHT))

eng_light = pygame.transform.scale(pygame.image.load(r"C:\Users\Admin\Desktop\pp2\main\images\пещерасвет.png"),(WIDTH,HEIGHT))

up_button = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\up_button.png'),(50,50))

walk_frames_left = [
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\1_move_left.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\2_move_left.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\3_move_left.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\4_move_left.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\5_move_left.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\6_move_left.png'), (200, 200))
]

walk_frames_right = [
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\1_move_right.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\2_move_right.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\3_move_right.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\4_move_right.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\5_move_right.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\animation_main\6_move_right.png'), (200, 200))
]

class Player:
    def __init__(self, x = x, y = y, speed = speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.player_rect = pygame.Rect(x, y, pers.get_width(), pers.get_height())
        self.walk_count = 0  # Счетчик кадров для анимации ходьбы
        self.last_update_time = pygame.time.get_ticks()  # Время последнего обновления анимации
        self.animation_delay = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.is_moving = True
            self.direction = 'left'
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.is_moving = True
            self.direction = 'right'
        else:
            self.is_moving = False

        # Обработка анимации ходьбы
        current_time = pygame.time.get_ticks()
        if self.is_moving and current_time - self.last_update_time > self.animation_delay:
            self.walk_count = (self.walk_count + 1) % len(walk_frames_left)
            self.last_update_time = current_time

        self.player_rect.update(self.x, self.y, pers.get_width(), pers.get_height())


    def draw(self, screen):
        # Отображение текущего кадра анимации ходьбы
        if self.is_moving:
            if self.direction == 'left':
                current_frame = walk_frames_left[self.walk_count % len(walk_frames_left)]
            elif self.direction == 'right':
                current_frame = walk_frames_right[self.walk_count % len(walk_frames_right)]
            screen.blit(current_frame, (int(self.x), int(self.y)))
        else:
            # Отображение статичного изображения игрока, если он не двигается
            # Здесь можно использовать изображение стоящего персонажа
            static_image = pers
            screen.blit(static_image, (int(self.x), int(self.y)))


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("minecraft.otf", size)


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)


def Den():
    x = 400
    y = 475
    speed = 10
    player = Player(x, y, speed)
    global took_umbrella

    running = True
    while running:
        #counter = Counter()
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player.player_rect.colliderect(invisible_umb_rect):
                    # При нажатии пробела и коллизии с зонтиком
                    took_umbrella = True  # Персонаж взял зонтик
                    player = Player_Umbrella(x, y, speed)
                if invisible_back_rect.colliderect(MENU_MOUSE_POS):
                    main.main()


            

        screen.fill((0,0,0))
        screen.blit(background,(0, 0))
        #pygame.draw.rect(screen, (255,255,255), invisible_back_rect)
        screen.blit(up_button,(500,250))
        #elapsed_time = counter.get_elapsed_time() // 1000  # Преобразование времени в секунды
        #draw_text(f"Time: {elapsed_time}s", get_font(30), (255, 255, 255), screen, 50, 50)

        #pygame.draw.rect(screen, (255,255,255), invisible_eng_rect)
        #pygame.draw.rect(screen, (255,255,255), invisible_umb_rect)

        player.update()
        
        player.draw(screen)
        if not took_umbrella:
            screen.blit(umb, (500, 325))
        
        if player.player_rect.colliderect(invisible_eng_rect):
            screen.blit(eng_light,(0,0))

        if player.player_rect.colliderect(invisible_umb_rect):
            if not took_umbrella:
                screen.blit(umb_light,(500,325))
                took_button_rect = pygame.Rect(750, 600, 150, 50)
                pygame.draw.rect(screen, (255, 255, 255), took_button_rect)
                draw_text("TAKE", get_font(30), (0, 0, 0), screen, 825, 625)
        pygame.display.flip()
        clock.tick(30)