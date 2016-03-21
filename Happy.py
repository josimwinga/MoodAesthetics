import pygame as pg
from pygame.locals import *
import PyParticles
from PyParticles import *
import time
import random
from datetime import datetime
import Menu
import Variables

def main():
    pg.init()
    pg.mixer.init()
    pg.mixer.music.load(Menu.Songs[3][0])
    pg.mixer.music.set_volume(Variables.currentVolume * .1)
    pg.mixer.music.play(0)
    
    windowWidth = Menu.windowWidth
    windowHeight = Menu.windowHeight
    
    frontColors= [(252,114,144), (252,205,215), (252, 73, 103), (225, 71, 108), (253, 253, 115),(249, 249, 149),(255, 241, 146)]
    
    
    bps = Menu.Songs[3][1]/60
    A=bps*2
    B=bps*4
    
    
    number = 20
    colors = []
    for n in range(number):
        color = Menu.color('Happy1')
        colors.append(color)
    
    print (colors)
    
    
    def happy():
        #top Circles
        pg.display.set_caption('Circles')
        screen = Menu.screen
        env = PyParticles.Environment((windowWidth, windowHeight))
        
        env.addParticles(number)
        env.addParticles(x=200, y=250, size=60, speed=500, angle=0)
        
        selected_particle = None
        running = True
        count =-1
        count2= -1
        count3=-1
        
        #Foreground Circles
        while pg.mixer.music.get_busy():
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
                elif event.type == pg.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pg.mouse.get_pos()
                    selected_particle = env.findParticle(mouseX, mouseY)
                elif event.type == pg.MOUSEBUTTONUP:
                    selected_particle = None
                elif event.type == KEYDOWN and event.key == pg.K_ESCAPE:
                    Variables.escape = True
                     
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
        
            musicPauseTime = pg.mixer.music.get_pos()
            
            while Variables.escape == True:
                pg.mixer.music.pause()
                Menu.escapeMenu()
                pg.mixer.music.play(0, musicPauseTime / 1000)
                
            while Variables.about == True:
                pg.mixer.music.pause()
                Menu.aboutMenu() 
                pg.mixer.music.play(0, musicPauseTime / 1000)            
     
            while Variables.settingsmenu == True:
                pg.mixer.music.pause()
                Menu.settingsMenu()
                pg.mixer.music.play(0, musicPauseTime / 1000)
                
            pg.mixer.music.set_volume(Variables.currentVolume * .1)
        
            
            "to make screen redraw your input"
            pg.display.flip()
            pg.time.Clock().tick(30)
            
    
    happy()

if __name__ == "__main__":    
    main() 