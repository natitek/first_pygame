# Example file showing a basic pygame "game loop"
import pygame

screen_width = 600
screen_height = 600
# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))



RED_TRIANGLE =  pygame.image.load("triangle.png")

bulletRect = pygame.rect.Rect(screen_width/2,screen_height/2,3,8)


class ship():
    def __init__(self,x,y,health=100):
        self.x =x
        self.y =y
        self.health = health
        self.cool_down = 0
    def draw(self, window):
        pygame.draw.rect(window,("red"),(self.x,self.y,50,50))
      
def main():
    running = True
    clock = pygame.time.Clock()

    # BULLET = pygame.draw.rect(screen,(255,255,255),bulletRect)
    def redraw_window():

        screen.blit(RED_TRIANGLE,(screen_width/2,screen_height))
        pygame.display.update()
    keys = pygame.key.get_pressed()
    while running:
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        # screen.fill((30,30,100))
        
    
        

        if keys[pygame.K_a]:
            pass
        elif keys[pygame.K_d]:
            pass
        elif keys[pygame.K_SPACE]:
            pass
        elif keys[pygame.K_ESCAPE]:
            running = False
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
main()

