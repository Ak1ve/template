from abc import abstractmethod, ABC

import pygame


class Drawable(ABC):
    @abstractmethod
    def draw(self, display: pygame.Surface):
        ...