## Jordan Thomas Acampado
## ASE 374K 

import pygame as pg
clock = pg.time.Clock()

pg.init()

#Define Shell for Pygame Engine (Replace with Quest AR Engine)
screen = pg.display.set_mode((1200, 600)) 
running = True
dt = 0 


#Image Defitions
background =  pg.image.load("Python_Thomas/Mars_back.webp").convert()

xlim = screen.get_width()
ylim = screen.get_height()

window = pg.image.load("Python_Thomas/Rect.png").convert_alpha()
slider = pg.image.load("Python_Thomas/slider.png").convert_alpha()

#Initiailize Classes
pg.display.set_caption('image')

class map(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y 
      
    def draw(self,screen):
       mapa = pg.transform.scale(window,(200,200))
       mapa.set_alpha(128)
       screen.blit(mapa, (self.x, self.y))

class vitals(object):
    def __init__(self,x,y, oxygen, power):
        self.x = x
        self.y = y 
        self.oxygen = oxygen
        self.power = power 
    def draw(self,screen):
       oxy = pg.transform.scale(window,(20,400))
       oxy.set_alpha(100)
       oxymeter = pg.transform.scale(slider,(20, (self.oxygen/100)*400))
       oxymeter.set_alpha(100)
       olim = oxy.get_height()
       o2lim = oxymeter.get_height()
       screen.blit(oxy, (30, 200))
       screen.blit(oxymeter, (30, 200 + olim - o2lim))
       

       volt = pg.transform.scale(window,(20,400))
       volt.set_alpha(100)
       voltmeter = pg.transform.scale(slider,(20, (self.power/100)*400))
       voltmeter.set_alpha(100)
       color = (255,0,0)
       vlim = volt.get_height()
       v2lim = voltmeter.get_height() 
       screen.blit(volt, (60, 200))
       screen.blit(voltmeter, (60, 200 + vlim - v2lim))
       #pg.draw.rect(screen, color, pg.Rect(60, 200 + vlim - (vlim *(self.power/100), 20, vlim * (self.power/100))))
            
       pg.draw.rect(screen, (0,0,0), pg.Rect(90, 200, 20, 300))
       pg.draw.rect(screen, color, pg.Rect(90, 200 + 300 - (self.power/100), 20,  300 * (self.power/100)))


    def tasks(self,screen):
        task = pg.transform.scale(window,(20,400))
        task.set_alpha(100)
        screen.blit(task, (400, 400))


class ui(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def draw(self,screen):
        color = (255,0,0)
        lg1 = pg.draw.rect(screen, color, pg.Rect(600, 600, 60, 60))
        
        
#Function Defintiions
def redrawGameWindow():
    mapb.draw(screen)
    vital.draw(screen)
    pg.display.update()

#Define UI Elements
mapb = map(30, 30)
vital = vitals(0,0, 80, 20)


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