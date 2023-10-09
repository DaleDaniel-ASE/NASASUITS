# -*- coding: utf-8 -*-

import pygame as pg

pg.init()

#SCENE 1 ______________________________________________________________________________
screen = pg.display.set_mode((700, 467))
clock = pg.time.Clock()
running = True
dt = 0 


        
def redrawGameWindow1():
 
count = 0

while running
    redrawGameWindow1()
    

#Initiailize Classes and Images
pg.display.set_caption('image')
    #Background
battle =  pg.image.load("/Users/dindoacampado/Downloads/bg_bdaman2.png").convert()
battle = pg.transform.scale(battle,(700,467))


        

def redrawGameWindow():
    pg.display.update()

while running
    
#EVENTS__________________________________________________________________
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
        
    screen.fill("black")

    dt = clock.tick(30)/1000
    redrawGameWindow()
pg.quit()