import pygame

from base.drawable import Drawable
from base.eventable import Eventable
from abc import ABC


class Window(Drawable, Eventable, ABC):
    def __init__(self, screen_size: tuple[int, int] = (500, 500), caption: str = "", fps: int = 60):
        pygame.init()
        self.screen_size = screen_size
        self.display = pygame.display.set_mode(screen_size)
        self.is_running = False
        self.fps = fps
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(caption)

    def start(self):
        self.is_running = True
        self.on_start()
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                self.on_event(event)

            self.update()
            self.display.fill((0, 0, 0))  # refill the screen with black
            self.draw(self.display)
            pygame.display.update()
            self.clock.tick(self.fps)
        self.on_exit()
