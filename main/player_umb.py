import pygame

pers = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист1.png')
pers = pygame.transform.scale(pers, (200, 200))


walk_frames_left = [
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист2 copy.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист3.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист4.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист5.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист6.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\лист7.png'), (200, 200))
]

walk_frames_right = [
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\листр2.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\листр3.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\листр4.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\листр5.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\листр6.png'), (200, 200)),
    pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\main\images\umb_animation\листр7.png'), (200, 200))
]


class Player_Umbrella:
    def __init__(self, x , y , speed):
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
