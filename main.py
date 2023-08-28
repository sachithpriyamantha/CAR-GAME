import pygame
from pygame.locals import *
import random


pygame.init()


#create the window
width = 500
height = 500
screan_size = (width, height)
screan = pygame.display.set_mode(screan_size)
pygame.display.set_caption('Car Game')