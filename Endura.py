import Global
import pygame
import math
import sys
import random
from Classes import Foliage, Player # importing all of the classes used (e.g player class
                      # and enemy classes)
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((1000,1000))

player1 = Player(500,500,5,20,20,100,1) #x,y,vel,width,height,health,damage
trees=[]
players=[player1]
for i in range(50):
    trees.append(Foliage(random.randint(-1000,1000),random.randint(-1000,1000), 50, 50, 400))

while True:# main loops for all of the game
    display.fill((165, 204, 176))

    for player in players:
        player.player_draw()
        player.player_movement()
        
    for tree in trees:
        tree.tree_draw()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
            exit()

    clock.tick(60)
    pygame.display.update()
    


