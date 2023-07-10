from abc import ABC

import pygame

from base.scene import Scene
from base.window import Window


class Game(Window):
    """
    A Game is an object that manages scenes.
    """
    def __init__(self, scene: Scene, screen_size: tuple[int, int] = (500, 500), caption: str = "", fps: int = 60):
        super().__init__(screen_size, caption, fps)
        self.scene = scene

    def on_start(self):
        self.scene.on_exit()

    def on_event(self, event: pygame.event.Event):
        self.scene.on_event(event)

    def draw(self, display: pygame.Surface):
        self.scene.draw(display)

    def on_exit(self):
        self.scene.on_exit()

    def update(self):
        self.scene.update()