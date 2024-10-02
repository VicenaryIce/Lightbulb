import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Hello World!')
bulbout = pygame.image.load('bulboff.png')
bulbon = pygame.image.load('bulbon.png')
bigbulbon = pygame.transform.scale(bulbon,(600,600))
bigbulbout = pygame.transform.scale(bulbout,(600,600))
on = False


screen.blit(bigbulbout,(0,0))






while True:
   for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
    
            #screen.clear()
            screen.blit(bigbulbon,(0,0))
            pygame.display.update()
            on == True
            
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill('white')

            screen.blit(bigbulbout,(0,0))
            pygame.display.update()
            on == False

            
            
        
         
        
   
   
   pygame.display.update()