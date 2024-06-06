import pygame , sys
from player import Player
import obstacle
from alien import Alien
class Game:
     def __init__(self):
          player_sprite = Player((screen_width/2,screen_height),5)
          self.player = pygame.sprite.GroupSingle(player_sprite)

          #obstacle setup
          self.shape = obstacle.shape
          self.block_size = 6
          self.blocks = pygame.sprite.Group()
          self.obstacle_amount = 4
          self.obstacle_x_positions = [num * (screen_width/self.obstacle_amount) for num in range(self.obstacle_amount)]
          self.create_multiple_obstacles(*self.obstacle_x_positions,x_start=screen_width/25,y_start=480)
        #   self.create_obstacle(40,480)

        #Alien. setup

          self.aliens = pygame.sprite.Group()
          self.alien_setup(rows = 6, cols = 8)

     def create_obstacle(self, x_start, y_start, offset_x):
          for row_index, row in enumerate(self.shape):
                for col_index , col in enumerate(row):
                     if col == 'x':
                          x = x_start + col_index * self.block_size + offset_x
                          y = y_start + row_index * self.block_size
                          block = obstacle.Block(self.block_size,(241,23,44),x,y)
                          self.blocks.add(block)
     def create_multiple_obstacles(self,*offset,x_start,y_start,):
          for offset_x in offset:
               self.create_obstacle(x_start,y_start,offset_x)
                     
     def alien_setup(self, rows, cols,x_distance = 60,y_distance = 40, x_offset= 70, y_offset= 100):
          for row_index, row in enumerate(range(rows)):
               for col_index, col in enumerate(range(cols)):
                    x = col_index * x_distance + x_offset
                    y = row_index * y_distance + y_offset
                    if row_index == 0: alien_sprite = Alien('yellow',x,y)
                    elif 1<= row_index <= 2: alien_sprite = Alien('green',x,y)
                    else: alien_sprite = Alien('blue',x,y)
                    self.aliens.add(alien_sprite)
     def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        
         
if __name__ == '__main__': #safeguard for multiple file apps
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()
    while True:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                    sys.exit()
        screen.fill((23,30,23))
     
        game.run()

        pygame.display.flip()
        clock.tick(60)