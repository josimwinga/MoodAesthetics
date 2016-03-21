'''
Created on Jul 17, 2013

@author: catapult
'''
import pygame as pg,sys
from pygame.locals import *
import Menu
import time
import Variables

pg.init()

def main():
    
    windowWidth = Menu.windowWidth
    windowHeight = Menu.windowHeight
    
    pg.mixer.init()
    
    screen = Menu.screen
    screen.fill((0, 0, 0))
    
    pg.mixer.music.load(Menu.Songs[1][0])
    bpm = Menu.Songs[1][0]
    pg.mixer.music.set_volume(Variables.currentVolume * .1)
    pg.mixer.music.play(0)
    
    red = 255
    green = 255
    blue = 255
    counter = 6
    thanks = 0
    
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    
    
    clicked = False
    while clicked == False:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                global click
                clicked = True
        click = Menu.Text((int(windowWidth/2), int(windowHeight/2)), (255, 255, 255), int(windowHeight/3), 'CLICK')
        click.draw()
        pg.display.flip()
        pg.time.Clock().tick(30) 
    
    escape = False

    while green >= counter + 1:
        for event in pg.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN and event.key == pg.K_ESCAPE:
                    Variables.escape = True
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                green = int(green - counter)
                blue = int(blue - counter)
                background.fill((red, green, blue))
        
        musicPauseTime = pg.mixer.music.get_pos()
        while Variables.escape == True:
            pg.mixer.music.pause()
            Menu.escapeMenu()
            background.fill((red, green, blue))
            pg.mixer.music.play(0, musicPauseTime / 1000)
            
        while Variables.about == True:
            pg.mixer.music.pause()
            Menu.aboutMenu() 
            background.fill((red, green, blue))
            pg.mixer.music.play(0, musicPauseTime / 1000)            
 
        while Variables.settingsmenu == True:
            pg.mixer.music.pause()
            Menu.settingsMenu()
            background.fill((red, green, blue))
            pg.mixer.music.play(0, musicPauseTime / 1000)
            
        pg.mixer.music.set_volume(Variables.currentVolume * .1)
                          
        screen.blit(background, (0, 0))
        
        pg.display.flip()
        pg.time.Clock().tick(30)
         
    Variables.angryMusicStopTime = pg.mixer.music.get_pos()
    return


    
if __name__ == "__main__":    
    main()