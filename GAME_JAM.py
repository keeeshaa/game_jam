import pygame
import sys
import main as main

pygame.init()

current_scene = None

def switch_scene(scene):
    global current_scene
    current_scene = scene


SCREEN = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Menu")

BG = pygame.image.load(r"C:\Users\Admin\Desktop\pp2\main\images\меню.jpg")
BG = pygame.transform.scale(BG, (1000, 700))  # Изменяем размер изображения на размер экрана

# Загрузка музыки
pygame.mixer.music.load(r"C:\Users\Admin\Desktop\pp2\main\sounds\про.mp3")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("minecraft.otf", size)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main_menu():
    # Воспроизведение музыки при отображении заставки
    pygame.mixer.music.play(-1)  # -1 означает бесконечное воспроизведение
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        draw_text("MAIN MENU", get_font(100), "#000000", SCREEN, 800, 400)

        # Draw buttons
        play_button_rect = pygame.Rect(700, 475, 200, 45)
        quit_button_rect = pygame.Rect(700, 525, 200, 45)

        #pygame.draw.rect(SCREEN, (215, 252, 212), play_button_rect)

        draw_text("PLAY", get_font(50), (0, 0, 0), SCREEN, 800, 500)
        draw_text("QUIT", get_font(50), (0, 0, 0), SCREEN, 800, 550)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(MENU_MOUSE_POS):
                    pygame.mixer.music.stop()  # Остановка музыки перед запуском игры
                    main.main()
                if quit_button_rect.collidepoint(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
