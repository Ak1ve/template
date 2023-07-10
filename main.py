import pygame

from base.game import Game
from base.scene import Scene
from base.entity import Entity

class ButtonEntity(Entity):
    def draw(self, display: pygame.Surface):
        x, y = self.position
        x1, y1 = x + 50, y + 50
        pygame.draw.rect(display, (255, 255, 255), (x, y, x1, y1))

    def update(self):
        self.x += 2
        self.y += 2


class MenuScene(Scene):
    def __init__(self):
        self.button_1 = ButtonEntity((0, 0))
        self.button_2 = ButtonEntity((20, 20))
        super().__init__([self.button_1, self.button_2])


class SimpleGame(Game):
    def __init__(self):
        super().__init__(MenuScene())


if __name__ == "__main__":
    game = SimpleGame()
    game.start()