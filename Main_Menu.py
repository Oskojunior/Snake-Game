import sys
import pygame


class MainMenu:
    def __init__(self):
        self.state = 0


    def change_state(self, change):
        if  (not (self.state == -2 and change == -1)) and (not(self.state == 0 and change == 1)):
            self.state += change

