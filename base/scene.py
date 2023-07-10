from typing import Protocol

import pygame

from base.eventable import Eventable
from base.drawable import Drawable


class EventableDrawable(Protocol):
    def on_start(self):
        pass

    def on_event(self, event: pygame.event.Event):
        pass

    def on_exit(self):
        pass

    def update(self):
        pass

    def draw(self, display: pygame.Surface):
        pass

    ...


class Scene(Eventable, Drawable):
    """
    A scene is what is being drawn to the screen.  It is managed by a Game object,
    and it itself manages objects
    """

    """
    # Experiment with this!  What makes the most sense?  would a list of objects make sense? or
    maybe we should do dict[str, EventableDrawable] instead and store a list of names to the object
    itself.  I.e. store a name with each object?
    scene = Scene({"character_name": Character()})
    scene.objects["character_name"].do_something() would be nice! 
    EXTRA BONUS:  Look into typed dicts and generic type parameters
    """

    def __init__(self, objects: list[EventableDrawable]):
        self.objects = objects

    def update(self):
        for obj in self.objects:
            obj.update()

    def draw(self, display: pygame.Surface):
        for obj in self.objects:
            obj.draw(display)

    def on_start(self):
        for obj in self.objects:
            obj.on_start()

    def on_exit(self):
        for obj in self.objects:
            obj.on_exit()

    def on_event(self, event: pygame.event.Event):
        for obj in self.objects:
            obj.on_event(event)
