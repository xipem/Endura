import pygame
import random
import Global
display = pygame.display.set_mode((1000,1000))
class Player():
    def __init__(self, player_x, player_y, player_vel ,player_width, player_height, player_health, player_damage):
        self.player_x = player_x
        self.player_y = player_y
        self.player_vel = player_vel
        self.player_width = player_width
        self.player_height = player_height
        self.player_health = player_health
        self.player_damage = player_damage
        
    def player_movement(self):#player movement by 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            Global.display_scroll[1] -= self.player_vel
            print(Global.display_scroll[1])
        if keys[pygame.K_s]:
            Global.display_scroll[1] += self.player_vel
            print(Global.display_scroll[1])
        if keys[pygame.K_a]:
            Global.display_scroll[0] -= self.player_vel
            print(Global.display_scroll[0])
        if keys[pygame.K_d]:
            Global.display_scroll[0] += self.player_vel
            print(Global.display_scroll[0])
        

    def player_draw(self):
       pygame.draw.rect(display, (255,255,255), (self.player_x, self.player_y, self.player_width, self.player_height))
        
    def player_stats(self):
        print(f"this player is at pos({self.player_x},{self.player_y}) and has a HP of {self.player_health}!")

        
class Foliage():
    def __init__(self, tree_x, tree_y, tree_width, tree_height, tree_health):
        self.tree_x = tree_x
        self.tree_y = tree_y
        self.tree_width = tree_width
        self.tree_height = tree_height
        self.tree_health = tree_health
        
    def tree_draw(self):
        pygame.draw.rect(display, (40,205,100), (self.tree_x-Global.display_scroll[0], self.tree_y-Global.display_scroll[1], self.tree_width, self.tree_height))
        
        
    
    

            
