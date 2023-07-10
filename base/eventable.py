"""

an Eventable is any object that has these events:
on_start()
on_event()
on_exit()
update()
"""
from abc import abstractmethod, ABC  # challenge: look into this!

import pygame


class Eventable(ABC):
    @abstractmethod
    def on_start(self):
        """
        This is called when the object is "started".  This is called by whatever
        object manages this class
        :return:
        """
        ...

    @abstractmethod
    def on_event(self, event: pygame.event.Event):
        """
        This is called whenever a pygame event is created by the player
        :param event:
        :return:
        """
        ...

    @abstractmethod
    def on_exit(self):
        """
        This is called whenever the object is "exiting"  This is called by whatever
        object manages this class
        :return:
        """
        ...

    @abstractmethod
    def update(self):
        """
        Called every frame
        :return:
        """
        ...
