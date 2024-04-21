import pygame


class Counter:
    def __init__(self):
        self.start_time = 0
        self.paused_time = 0
        self.is_paused = False

    def start(self):
        self.start_time = pygame.time.get_ticks()  # Устанавливаем начальное время как текущее время
        self.paused_time = 0
        self.is_paused = False

    def pause(self):
        if not self.is_paused:
            self.paused_time = pygame.time.get_ticks() # Запоминаем прошедшее время
            self.is_paused = True

    def resume(self):
        if self.is_paused:
            self.start_time = pygame.time.get_ticks() - self.paused_time  # Восстанавливаем начальное время
            self.is_paused = False

    def get_elapsed_time(self):
        if not self.is_paused:
            return self.start_time  # Текущее прошедшее время
        else:
            return self.paused_time  # Возвращаем сохраненное время при паузе
