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

def main():
    pg.init()
    pg.mixer.init()
    
    pg.mixer.music.load(Menu.Songs[4][0])
    pg.mixer.music.set_volume(Variables.currentVolume * .1)
    pg.mixer.music.play(0)
    
    windowWidth = Menu.windowWidth
    windowHeight = Menu.windowHeight
    screen = Menu.screen
    screen.fill(Menu.color('SadBackground'))
    
    bpm = (Menu.Songs[4][1])
    bps = bpm /60
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
        
    
    
    edge = int(windowWidth / (6 + 2/3))
    width = windowWidth * .3
    x1 = edge + width
    x2 = windowWidth * .5 - width * .5
    x3 = windowWidth - edge
    y1 = windowHeight * .5 - .25 * width * math.sqrt(3)
    y2 = windowHeight * .5 + .25 * width * math.sqrt(3) 
    y3 = windowHeight * .5 - .25 * width * math.sqrt(3) 
    
    
    
    #Triangles Draw
    "insert shape, then put a background fill between each shape if you w    ant background to always flash, then time sleep for bpm"
    
    counter = 0
    escape = False
    while pg.mixer.music.get_busy():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                Variables.escape = True
        i = counter % 10
        if counter % 120 <= 9:
            triN2(i+1, 1000, 0, 11000)
        
        if counter % 120 >= 10 and counter <= 14:
            triN(i+1, x2, y2, 78000)  
            triN2(i+1, x3, y3, 4050)
             
        if counter % 120 >=15 and counter <= 19:
            triN2(i+1, x3, y3, 9854)
            triN2(i+1, x3, y3, 18504)
            
        if counter % 120 >= 20 and counter <= 24:
            triN(i+1, 1000, 0, 11000)
            triN2(i+1, x1, y1, 7000)
            triN(i+1, x2, y2, 28000)
             
        if counter % 120 >= 25 and counter <= 29:   
            triN2(i+1, x3, y3, 10000)
            triN2(i+1, x1, y1, 1000)
            triN(i+1, x2, y2, 2012)
        if counter % 120 >= 30 and counter <= 34: 
            triN(i+1, x3, y3, 970)
            triN2(i+1, 1000, 0, 11000)
            triN2(i+1, x1, y1, 4568)
            triN2(i+1, 1000, 0, 11000)
           
        if counter % 120 >= 35 and counter <= 39:   
            triN2(i+1, x1, y1, 5760)
            triN(i+1, x2, y2, 8000)
        if counter % 120 >= 40 and counter <= 44:
            triN2(i+1, 1000, 0, 11000)
        if counter % 120 >= 45 and counter <= 49:
            triN(i+1, x2, y2, 9000)
            triN(i+1, x1, y1, 5760)
            triN(i+1, 100, 700, 11000)
            triN2(i+1, x3, y3, 8000)
        if counter % 120 >= 50 and counter <= 54:
            triN2(i+1, x1, y1, 1054)
            triN(i+1, x2, y2, 900)
            triN2(i+1, 1000, 0, 11000)
        if counter % 120 >= 55 and counter <= 59:
            triN2(i+1, x3, y3, 10000)
            triN(i+1, x1, y1, 9500)
            triN2(i+1, x2, y2, 9000)
        if counter % 120 >= 60 and counter <= 64: 
            triN(i+1, 1000, 0, 11000)
            triN2(i+1, x1, y1, width)
            triN(i+1, 100, 700, 11000) 
            
        if counter % 120 >= 65 and counter <= 69:
            triN(i+1, x2, y2, 78000)  
            triN2(i+1, x3, y3, 4050)
            triN(i+1, x2, y2, 8000) 
        if counter % 120 >=70 and counter <= 79:
            triN2(i+1, x3, y3, 9854)
            triN(i+1, x2, y2, 20500)
            triN(i+1, 100, 700, 11000)
            triN2(i+1, x3, y3, 8504)
            triN(i+1, x3, y3, 970)
            
        if counter % 120 >= 80 and counter <= 89:
            triN2(i+1, 1000, 0, 11000)
            triN2(i+1, x1, y1, 4568)
            triN2(i+1, 1000, 0, 11000)
            triN2(i+1, 1000, 0, 11000)
        
        if counter % 120 >= 90 and counter <= 99:
            triN(i+1, x2, y2, 78000)  
            triN2(i+1, x3, y3, 4050)
            triN2(i+1, x3, y3, 9854) 
   
        if counter % 120 >=100 and counter <= 109:
            triN(i+1, x2, y2, 20500)
            triN2(i+1, x3, y3, 8504)
            triN2(i+1, x3, y3, 8504)
            triN(i+1, x3, y3, 970)
            triN2(i+1, 1000, 0, 11000)
            
        if counter % 120 >= 110 and counter <= 119:
            triN(i+1, 1000, 0, 11000)
            triN2(i+1, x1, y1, 7000)
            triN(i+1, x2, y2, 28000)
            
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
            
        counter = counter + 1
        pg.time.Clock().tick(bps) 
    
        pg.display.flip()
if __name__ == "__main__":    
    main()
        
