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

#colors
grey = (100, 100, 100)
darkgreen = (0,100,0)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)
darkgray = (169,169,169)
dodgerblue4 = (16,78,139)


#game setting
gameover = False
speed = 2
score = 0

#markers size
marker_width = 10
marker_height = 50

#road and edge markers
road = (100, 0, 300, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

#game loop
clock = pygame.time.Clock()
fps = 120
running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    

    #drow the grass
    screan.fill(darkgreen)

    #draw the road
    pygame.draw.rect(screan, darkgray, road)

    #draw the edge marker
    pygame.draw.rect(screan, dodgerblue4, left_edge_marker)
    pygame.draw.rect(screan, dodgerblue4, right_edge_marker)

    pygame.display.update()

pygame.quit()