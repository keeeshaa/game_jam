import pygame
import sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

#Setting up Fonts
font = pygame.font.SysFont("comicsans", 60)
font_small = pygame.font.SysFont("comicsans", 20)
game_over = font.render("Game Over", True, WHITE)

pygame.mixer.Sound(r'C:\Users\Admin\Desktop\pp2\lab8\racer\background.wav').play() #background sound

background = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\rain\background_rain.JPG'),(401, 605)) #background image
invisible_line_y = 550

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Save the stars")


#Creating coins and functions for them
class drop(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r'C:\Users\Admin\Desktop\pp2\rain\rain.png')# coin image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0) # randomly generated coins

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
      def respawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


#Creating a player's sprite and functions for it
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load(r'C:\Users\Admin\Desktop\pp2\rain\pixel_sprite_rain.png'),(200,200))# image of the player's sprite
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    #Function to move the sprite
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
P1 = Player()
C1 = drop()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(C1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

#Game Loop
def Rain():
    while True:

        #Cycles through all events occuring  
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                  SPEED += 0.5      
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        #displaying scores and the amount of coins collected
        DISPLAYSURF.blit(background, (0,0))
        scores = font_small.render(str(SCORE), True, WHITE)
        DISPLAYSURF.blit(scores, (10,10))
        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            entity.move()
            DISPLAYSURF.blit(entity.image, entity.rect)
        for entity in coins:
            if entity.rect.bottom > invisible_line_y:
                # Game over condition if a drop crosses the line
                DISPLAYSURF.blit(game_over, (30, 250))  # Display "Game Over" message
                pygame.display.update()  # Update the display
                pygame.time.delay(1000)
                pygame.quit()  # Quit pygame
                sys.exit()
        #To be run if collision occurs between Player and Coin
        if pygame.sprite.spritecollideany(P1, coins):
              pygame.mixer.Sound(r'C:\Users\Admin\Desktop\pp2\lab8\racer\coin_collect.mp3').play()
              SCORE += 1  
              for entity in coins:
                    entity.respawn() 
              pygame.display.update()
        pygame.display.update()
        if SCORE == 20:
            pygame.quit()
        FramePerSec.tick(FPS)
