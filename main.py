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

# x coordinated of lanes
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

#for animating movement of the lane marker
lane_marker_move_y = 0

class Vehical(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)


        #scale the image down so if fits in the lane
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class PlayerVehical(Vehical):
    def __init__(self, x, y):
        image = pygame.image.load('images/car.png')
        super().__init__(image, x, y)

#player's starting coodinates
player_x = 250
player_y = 410


#create the player's car
player_group = pygame.sprite.Group()
player = PlayerVehical(player_x, player_y)
player_group.add(player)

#load the other vehical
image_filename = ['truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
vehical_image = []
for image_filename in image_filename:
    image = pygame.image.load('images/' + image_filename)
    vehical_image.append(image)

#sprite group for vehical
vehical_group = pygame.sprite.Group()


#game loop
clock = pygame.time.Clock()
fps = 120
running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


        #move the players car using the left keys
        if event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100
    

    #drow the grass
    screan.fill(darkgreen)

    #draw the road
    pygame.draw.rect(screan, darkgray, road)

    #draw the edge marker
    pygame.draw.rect(screan, dodgerblue4, left_edge_marker)
    pygame.draw.rect(screan, dodgerblue4, right_edge_marker)


    #draw the lane marker
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screan, white, (left_lane + 45, y+ lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screan, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))


    #draw the player's car
    player_group.draw(screan)


    #add up to two vehical
    if len(vehical_group) < 2:
        add_vehical = True
        for vehical in vehical_group:
            if vehical.rect.top < vehical.rect.height * 1.5:
                add_vehical = False

        if add_vehical:

            #select random lane
            lane = random.choice(lanes)

            #select a random vehical image
            image = random.choice(vehical_image)
            vehical = Vehical(image, lane, height / -2)
            vehical_group.add(vehical)



    #make the vehical move
    for vehical in vehical_group:
        vehical.rect.y += speed

        #remove the vehical once it goes off screan

        if vehical.rect.top >= height:
            vehical.kill()

            #add to score
            score += 1

            #speed up the game after passing 5 vehicals
            if score > 0 and score % 5 == 0:
                speed += 1

    #draw the vehicals
    vehical_group.draw(screan)

    #display the score
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 450)
    screan.blit(text, text_rect)



    pygame.display.update()

pygame.quit()