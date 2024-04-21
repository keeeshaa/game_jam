import pygame
import sys
from pygame.locals import *
import random
from maze_main import maze
from den import Den
from tree_main import Tree
#from counter import Counter

pygame.init()

clock = pygame.time.Clock()
time = 0

#pygame.mixer.Sound(r'').play() #background sound

x = 0
y = 400
speed = 10

invisible_enter_rect = pygame.Rect(720, 450, 100, 100)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

atmo = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\light.png')

back = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\forest.JPEG')
back = pygame.transform.scale(back, (SCREEN_WIDTH, SCREEN_HEIGHT))

pers = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\player.png')
pers = pygame.transform.scale(pers, (200, 200))

enter = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\деревосвет.png')
enter = pygame.transform.scale(enter, (SCREEN_WIDTH, SCREEN_HEIGHT))


invisible_enter_rect = pygame.Rect(720,450,100,100)


#Buttons
up = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\вверх.png'),(750,750))
down = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\вниз.png'),(750,750))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("minecraft.otf", size)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)


class MovingImage:
    def __init__(self):
        self.x = random.randint(-30, SCREEN_WIDTH - 30)
        self.y = random.randint(-30, SCREEN_HEIGHT - 30)
        self.speed_x = random.randint(1, 2) or random.randint(-1, 0)  # Случайная скорость по оси X
        self.speed_y = random.randint(-1, 0) or random.randint(1, 2) # Случайная скорость по оси Y

    def update(self):
        # Движение изображения
        self.x += self.speed_x
        self.y += self.speed_y


    def draw(self):
        screen.blit(atmo, (self.x, self.y))

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

objects = []
def main():
    global time
    x = 0
    y = 400
    speed = 10
    player = Player(x, y, speed)
    #counter = Counter()
    running = True
    while running:
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():    
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if up_button_rect.collidepoint(MENU_MOUSE_POS):
                    Tree()
                if down_button_rect.collidepoint(MENU_MOUSE_POS):
                    Den()

        # Generate new objects randomly
        if random.random() < 0.012:
            new_object = MovingImage()
            objects.append(new_object)

        screen.fill((0,0,0))
        screen.blit(back, (0, 0))
        #counter.start()
        #elapsed_time = counter.get_elapsed_time() // 1000  # Преобразование времени в секунды
        #draw_text(f"Time: {elapsed_time}s", get_font(30), (255, 255, 255), screen, 50, 50)

        #player_rect = pygame.Rect(x, y, 200, 200)  # Прямоугольник для игрока
        if player.player_rect.colliderect(invisible_enter_rect):
            up_button_rect = pygame.Rect(939, 380, 30, 41)
            down_button_rect = pygame.Rect(939, 430, 30, 41)
            screen.blit(enter, (0, 0))
            screen.blit(up,(300,70))
            screen.blit(down,(300,70))
            

        player.update()
        player.draw(screen)
        #pygame.draw.rect(screen, (255,255,255), invisible_enter_rect)
        #pygame.draw.rect(screen, (215, 252, 212), up_button_rect)
        #pygame.draw.rect(screen, (215, 252, 212), down_button_rect)

        for obj in objects:
            obj.update()
            obj.draw()
        # Draw the main character on top
        # Draw the player character

        pygame.display.update()
        clock.tick(30)


        

