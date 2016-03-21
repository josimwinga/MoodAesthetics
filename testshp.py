import pygame as pg
from pygame.locals import *
import PyParticles
from PyParticles import *
import time
import random
from datetime import datetime
import Menu

frontColors= [(252,114,144), (252,205,215), (252, 73, 103), (225, 71, 108), (253, 253, 115),(249, 249, 149),(255, 241, 146)]
def randomColor(colors):
    i=random.randrange (0, len(frontColors))
    color=colors[i]
    return color
#speed based on music
bpm=1 
#Songs[0][1]/60
A=bpm
B=bpm/2


number = 20
colors = []
for n in range(number):
    color = Menu.color('Happy1')
    colors.append(color)

print (colors)


def happy():
    #top Circles
    pg.display.set_caption('Circles')
    screen=pg.display.set_mode((windowWidth,windowHeight))
    env = PyParticles.Environment((windowWidth, windowHeight))
    
    env.addParticles(number)
    env.addParticles(x=200, y=250, size=60, speed=500, angle=0)
    
    selected_particle = None
    running = True
    count =-1
    count2= -1
    count3=-1
    
    #Foreground Circles
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pg.mouse.get_pos()
                selected_particle = env.findParticle(mouseX, mouseY)
            elif event.type == pg.MOUSEBUTTONUP:
                selected_particle = None
        #count +=1
        #if count %3 == 0:
        #    time.sleep(.23)
           
            
                        
    
        env.update()
        screen.fill(env.colour)
    
        count +=1
        if count %A == 0:
                colx = Menu.color('Happy1') 
        count2 +=1
        if count %B == 0:
                colz = Menu.color('Happy2')  
                
    #Co1 1
        pg.draw.circle(screen, colx, [125, 100], 60)
        pg.draw.circle(screen, colz, [125, 300], 60)
        pg.draw.circle(screen, colx, [125, 500], 60)
    #col 2
        pg.draw.circle(screen, colz, [375, 100], 60)
        pg.draw.circle(screen, colx, [375, 300], 60)
        pg.draw.circle(screen, colz, [375, 500], 60)
    #col 3
        pg.draw.circle(screen, colx, [625, 100], 60)
        pg.draw.circle(screen, colz, [625, 300], 60)
        pg.draw.circle(screen, colx, [625, 500], 60)
    #col4
        pg.draw.circle(screen, colz, [875, 100], 60)
        pg.draw.circle(screen, colx, [875, 300], 60)
        pg.draw.circle(screen, colz, [875, 500], 60)
    
    
        count3 +=1
        if count3 %50 == 0:
                coly = Menu.color('') 
        if selected_particle:
            (mouseX, mouseY) = pg.mouse.get_pos()
            selected_particle.mouseMove(mouseX, mouseY)
        for p in env.particles:
            index = env.particles.index(p)
            print (index)
            if index < 20:
                coly = colors[index]
            else:
                coly = colors[19]          
            pg.draw.circle(screen, coly, (int(p.x), int(p.y)), p.size, p.thickness)
    
    
        
        "to make screen redraw your input"
        pg.display.flip()
        pg.time.Clock().tick(30)
        

happy()

       
