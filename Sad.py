'''
Created on Jul 19, 2013

@author: catapult
'''
import pygame as pg,sys
from pygame.locals import *
import Menu
import Variables

pg.init()

def main():
    colors1 = []
    points1 = []
    colors2 = []
    points2 = []
    pg.mixer.init()
    
    pg.mixer.music.load(Menu.Songs[2][0])
    pg.mixer.music.set_volume(Variables.currentVolume * .1)
    pg.mixer.music.play(0)
    
    #base script
    
    xOne=Menu.windowWidth
    xTwo=Menu.windowWidth
    y=Menu.windowHeight
    
    dxOne=5
    dxTwo=2
    
    #screen
    screen = Menu.screen
    clock=pg.time.Clock()
    screen.fill(Menu.color('SadBackground'))
    
    color1 = Menu.color('Sad')
    color2 = Menu.color('Sad')
    while color1 == color2:
        print ('Same Color')
        color1 = Menu.color('Sad')
    
    while pg.mixer.music.get_busy():
        clock.tick(30)
        if xOne > 4000:
            dxOne= -5
            lastcolor1 = color1
            color1 = Menu.color('Sad')
            while color1 == lastcolor1:
                color1 = Menu.color('Sad')
    
        if xOne < Menu.windowWidth:
            dxOne=5
            lastcolor1 = color1
            color1 = Menu.color('Sad')
            while color1 == lastcolor1:
                color1 = Menu.color('Sad')
    
        if xTwo > Menu.windowWidth:
            dxTwo = -2
            lastcolor2 = color2
            color2 = Menu.color('Sad')
            while color2 == lastcolor2:
                color2 = Menu.color('Sad')
    
        if xTwo < 200:
            dxTwo = 2
            lastcolor2 = color2
            color2 = Menu.color('Sad')
            while color2 == lastcolor2:
                color2 = Menu.color('Sad')
        
        colors1.append(color1)
        colors2.append(color2)  
        points1.append((xOne, y)) 
        points2.append((xTwo, y)) 
            
        pg.draw.line(screen, color1,(0,0), (xOne,y), 4)
        pg.draw.line(screen, color2,(0, 0), (xTwo, y), 4)    
        
        xOne = xOne + dxOne
        xTwo = xTwo + dxTwo
        pg.display.update()
        
        for event in pg.event.get():
            if event.type==pg.QUIT:
                return
            if event.type == KEYDOWN and event.key == pg.K_ESCAPE:
                    Variables.escape = True
        
        musicPauseTime = pg.mixer.music.get_pos()
        while Variables.escape == True:
            pg.mixer.music.pause()
            Menu.escapeMenu()
            screen.fill(Menu.color('SadBackground'))
            for i in range(len(colors1)):
                pg.draw.line(screen, colors1[i],(0,0), points1[i], 4)
                pg.draw.line(screen, colors2[i],(0,0), points2[i], 4)
            pg.mixer.music.play(0, musicPauseTime / 1000)
            
        while Variables.about == True:
            pg.mixer.music.pause()
            Menu.aboutMenu() 
            screen.fill(Menu.color('SadBackground'))
            for i in range(len(colors1)):
                pg.draw.line(screen, colors1[i],(0,0), points1[i], 4)
                pg.draw.line(screen, colors2[i],(0,0), points2[i], 4)
            pg.mixer.music.play(0, musicPauseTime / 1000)            
 
        while Variables.settingsmenu == True:
            pg.mixer.music.pause()
            Menu.settingsMenu()
            screen.fill(Menu.color('SadBackground'))
            for i in range(len(colors1)):
                pg.draw.line(screen, colors1[i],(0,0), points1[i], 4)
                pg.draw.line(screen, colors2[i],(0,0), points2[i], 4)
            pg.mixer.music.play(0, musicPauseTime / 1000)
            
        pg.mixer.music.set_volume(Variables.currentVolume * .1)
                
if __name__ == "__main__":    
    main()
