import pygame , sys
from player import Player
import obstacle

class Game:
     def __init__(self):
          #player setup
          player_sprite = Player((screen_width/2,screen_height),5)
          self.player = pygame.sprite.GroupSingle(player_sprite)

          #obstacle setup
          self.shape = obstacle.shape
          self.block_size = 6
          self.blocks = pygame.sprite.Group()
          self.create_obstacle(40,480)

     def create_obstacle(self, x_start, y_start):
          for row_index, row in enumerate(self.shape):
                for col_index , col in enumerate(self.shape):
                     if col == 'x':
                          x = col_index * self.block_size
                          y = row_index * self.block_size
                          block = obstacle.Block(self.block_size,(241,23,44),x,y)
                          self.blocks.add(block)
        
     def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        
         
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