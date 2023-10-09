## Jordan Thomas Acampado
## ASE 374K 

import pygame as pg
clock = pg.time.Clock()

pg.init()

#Define Shell for Pygame Engine (Replace with Quest AR Engine)
screen = pg.display.set_mode((1500, 600)) 

running = True
dt = 0 


#Initiailize Classes and Images 
pg.display.set_caption('image')

class map(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
          
    def draw(self,screen):
       surface = pg.display.set_mode((self.x,self.y))
       color = (255,0,0)
       pg.draw.rect(surface, color, pg.Rect(30, 30, 60, 60))

    #Background 
background =  pg.image.load("Python_Thomas/Mars_back.webp").convert()
#background = pg.transform.scale(background,(700,467))
        

def redrawGameWindow():
    mapb.draw(screen)
    pg.display.update()


mapb = map(0, 0) 
## Main Function
while running:   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
        
## Display Mars Background (Replace with AR Field)
    screen.fill("black")
    screen.blit(background,(0,0)) 

    dt = clock.tick(30)/1000
    redrawGameWindow()
pg.quit()