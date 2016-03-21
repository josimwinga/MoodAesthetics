'''
Created on Jul 18, 2013

@author: catapult
'''

import time
import random
import math
import pygame as pg
import pygame.gfxdraw
import Menu
import Variables

pg.init()
pg.mixer.init()

pg.mixer.music.load(Menu.Songs[4][0])
pg.mixer.music.set_volume(Variables.currentVolume * .1)
pg.mixer.music.play(0)

windowWidth = Menu.windowWidth
windowHeight = Menu.windowHeight
screen = Menu.screen

bpm = (Menu.Songs[4][1])
bps = bpm / 60
    
#Triangle 1 
def equilateralTriangle(lowerLeftX, lowerLeftY, width):
    x1=lowerLeftX
    y1=lowerLeftY
    x2=x1+width
    y2=y1
    x3=x1+width/2
    y3=y1-width*math.sqrt(3)/2
    points= [(x1,y1), (x2,y2), (x3,y3)]
    color = Menu.color('Chill')
    pg.gfxdraw.aapolygon(screen, points, color)
    pg.gfxdraw.filled_polygon(screen, points, color)


def triN(n, lowerLeftX, lowerLeftY, width):
    if n <=1:
        equilateralTriangle(lowerLeftX, lowerLeftY, width)
    else:    
        triN(n-1, lowerLeftX, lowerLeftY, width/2)
        triN(n-1, lowerLeftX + width/2, lowerLeftY, width/2)
        triN(n-1, lowerLeftX + width/4, lowerLeftY - math.sqrt(3) / 2 * width /2, width/2)
        
#Triangle 2 
def equilateralTriangle2(upperRightX, upperRightY, width):
    x1=upperRightX
    y1=upperRightY
    x2=x1-width
    y2=y1
    x3=x1-width/2
    y3=y1+width*math.sqrt(3)/2
    
    points= [(x1,y1), (x2,y2), (x3,y3)]
    
    color = Menu.color('Chill')
    pg.gfxdraw.aapolygon(screen, points, color)
    pg.gfxdraw.filled_polygon(screen, points, color)


def triN2(n, upperRightX, upperRightY, width):
    if n <=1:
        equilateralTriangle2(upperRightX, upperRightY, width)
    else:    
        triN2(n-1, upperRightX, upperRightY, width/2)
        triN2(n-1, upperRightX - width/2, upperRightY, width/2)
        triN2(n-1, upperRightX - width/4, upperRightY + math.sqrt(3) / 2 * width / 2, width/2)

triangleTypes = ['BigUp', 'BigDown', 'SmallUp', 'SmallDown']

def drawTriangle(type):
    if type == 'BigUp':
        n = random.randrange(3, 7)
        x = random.randrange(0, int(5 * windowWidth / 6))
        y = random.randrange(0, int(5 * windowHeight / 6))
        size = random.randrange(int(windowWidth / .6), int(windowWidth * 5))
        
        triN(n, x, y, size)
        
    elif type == 'BigDown':
        n = random.randrange(3, 7)
        x = random.randrange(int(1 * windowWidth / 6), windowWidth)
        y = random.randrange(int(1 * windowHeight / 6), windowHeight)
        size = random.randrange(int(windowWidth / .6), int(windowWidth * 5))
        
        triN2(n, x, y, size)
        
    elif type == 'SmallUp':
        n = random.randrange(3, 7)
        x = random.randrange(0, int(99 * windowWidth / 100))
        y = random.randrange(0, int(99 * windowHeight / 100))
        size = random.randrange(int(windowWidth / 10), int(windowWidth / 2))
        
        triN(n, x, y, size)
        
    elif type == 'SmallDown':
        n = random.randrange(3, 7)
        x = random.randrange(int(1 * windowWidth / 100), windowWidth)
        y = random.randrange(int(1 * windowHeight / 100), windowHeight)
        size = random.randrange(int(windowWidth / 10), int(windowWidth / 2))
        
        triN2(n, x, y, size)


def main():

    while pg.mixer.music.get_busy():
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    Variables.escape = True
        
        type = random.choice(triangleTypes)
        print(type)
        drawTriangle(type)

        
        musicPauseTime = pg.mixer.music.get_pos()
        while Variables.escape == True:
            pg.mixer.music.pause()
            Menu.escapeMenu()
            screen.fill((0, 0, 0))
            pg.mixer.music.play(0, musicPauseTime / 1000)
           
        while Variables.about == True:
            pg.mixer.music.pause()
            Menu.aboutMenu() 
            screen.fill((0, 0, 0))
            pg.mixer.music.play(0, musicPauseTime / 1000)            
    
        while Variables.settingsmenu == True:
            pg.mixer.music.pause()
            Menu.settingsMenu()
            screen.fill((0, 0, 0))
            pg.mixer.music.play(0, musicPauseTime / 1000)
           
        pg.mixer.music.set_volume(Variables.currentVolume * .1)
        
        pg.time.Clock().tick(bps)
        pg.display.flip()
    
if __name__ == "__main__":    
    main()