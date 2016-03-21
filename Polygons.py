'''
Created on Jul 19, 2013

@author: catapult
'''
import math, random, pygame as pg, time
from pygame.locals import *
import Menu
import pygame.gfxdraw
import Variables


def main():

    pg.init()
    pg.mixer.init()
    
    polygons = []
    colors = []
    
    windowWidth = Menu.windowWidth
    windowHeight = Menu.windowHeight
    
    screen = Menu.screen
    screen.fill((0, 0, 0))
    
    pg.mixer.music.load(Menu.Songs[1][0])
    pg.mixer.music.set_volume(Variables.currentVolume * .1)
    pg.mixer.music.play(0, Variables.angryMusicStopTime / 1000)            
    pg.mixer.music.play(0)
    bpm = Menu.Songs[1][1]
    
    
    while pg.mixer.music.get_busy():
        
        for event in pg.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN and event.key == pg.K_ESCAPE:
                    Variables.escape = True
        
        points = []
        for i in range(random.randrange(3, 7)):
            newPoint = (random.randrange(0, windowWidth), random.randrange(0, windowHeight))
            points.append(newPoint)
        polygons.append(points)
        
        newcolor = Menu.color('Angry')
        colors.append(newcolor)
        pg.gfxdraw.aapolygon(screen, points, newcolor)
        pg.gfxdraw.filled_polygon(screen, points, newcolor)
        
        musicPauseTime = pg.mixer.music.get_pos()
        while Variables.escape == True:
            pg.mixer.music.pause()
            Menu.escapeMenu()
            screen.fill((0, 0, 0))
            for i in range(len(colors)):
                pg.gfxdraw.aapolygon(screen, polygons[i], colors[i])
                pg.gfxdraw.filled_polygon(screen, polygons[i], colors[i])
            pg.mixer.music.play(0, musicPauseTime / 1000)
            
        while Variables.about == True:
            pg.mixer.music.pause()
            Menu.aboutMenu() 
            screen.fill((0, 0, 0))
            for i in range(len(colors)):
                pg.gfxdraw.aapolygon(screen, polygons[i], colors[i])
                pg.gfxdraw.filled_polygon(screen, polygons[i], colors[i])
            pg.mixer.music.play(0, musicPauseTime / 1000)            
 
        while Variables.settingsmenu == True:
            pg.mixer.music.pause()
            Menu.settingsMenu()
            screen.fill((0, 0, 0))
            for i in range(len(colors)):
                pg.gfxdraw.aapolygon(screen, polygons[i], colors[i])
                pg.gfxdraw.filled_polygon(screen, polygons[i], colors[i])
            pg.mixer.music.play(0, musicPauseTime / 1000)
            
        pg.mixer.music.set_volume(Variables.currentVolume * .1)

        pg.display.flip()
        pg.time.Clock().tick(bpm / 30) 
    
    time.sleep(1)
    
if __name__ == "__main__":    
    main()
    
