import pygame

from base.drawable import Drawable
from base.eventable import Eventable


class BaseEntity:
    def __init__(self, position: tuple[int, int]):
        self.position = position

    @property
    def x(self) -> int:
        return self.position[0]

    @x.setter
    def x(self, value: int):
        self.position = (value, self.y)

    @property
    def y(self) -> int:
        return self.position[1]

    @y.setter
    def y(self, value: int):
        self.position = (self.x, value)


class Entity(BaseEntity, Drawable, Eventable):
    def draw(self, display: pygame.Surface):
        pass

    def on_start(self):
        pass

    def on_event(self, event: pygame.event.Event):
        pass

    def on_exit(self):
        pass

    def update(self):
        pass
