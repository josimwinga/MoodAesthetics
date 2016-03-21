'''
Mood Aesthetics
Started on July 15, 2013
@author: Team Best Team
'''

import math, random, pygame as pg
from pygame.locals import *
pg.init()
pg.mixer.init()
import Angry
import Sad
import Polygons
import Happy
import Variables
import Chill

windowHeight = 600
windowWidth = 1000

Songs = [
        ['Music/Menu3.ogg', 152],
        ['Music/Angry.ogg', 144],
        ['Music/Sad2.ogg', 112],
        ['Music/Happy.ogg', 120],
        ['Music/Chill.ogg', 105] 
        ]
        
titles = []
moodOne = 0
moodTwo = 0
moodThree = 0
moodFour = 0

preferences = 0
title = 0
about = 0
quit = 0
bpm = 0

screen = pg.display.set_mode([windowWidth, windowHeight])

def color(emotion):
    if emotion == 'Random':
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    elif emotion == 'Happy1':
        happyColors1=[(224,246,115), (212,255,0), (231,253,114), (245, 253, 206), (192,242,75), (199,245,239), (0, 205, 215), (111, 245, 227), (0,152,131)]
        return random.choice(happyColors1)
    elif emotion == 'Happy2':
        happyColors2=[(252,114,144), (252,205,215), (252, 73, 103), (225, 71, 108), (253, 253, 115),(249, 249, 149),(255, 241, 146)]
        return random.choice(happyColors2)
    elif emotion == 'Sad':
        sadColors = [(206, 235, 239), (145, 162, 165), (61, 92, 97), (163, 215, 223), (97, 114, 125), (150, 147, 230), (132, 130, 179), (73, 71, 155),  (45, 42, 139), (70, 6, 104), (154, 146, 186), (129, 128, 132), (72, 72, 75), (47, 46, 48)]
        return random.choice(sadColors)
    elif emotion == 'SadBackground':
        return (41, 46, 46)
    elif emotion == 'Angry':
        gray= random.randrange(0, 256)
        GB= random.randrange(0, 15)
        angrycolors = [(random.randrange(0, 256), 0, 0), (gray, gray, gray), (random.randrange(0, 256), GB, GB), (random.randrange(15, 256), 8, 8), (10, 10, 10), (0, 0, 0)]
        return random.choice(angrycolors)
    elif emotion == 'Chill':
        chillColors = [(251, 202, 134), (222, 235, 220), (154, 212, 239), (207, 216, 220), (65, 73, 76), (161, 152, 146),(152, 32, 108), (202, 75, 160)]
        return random.choice(chillColors)

def menu():
    
    screen.fill(pg.Color('Black'))
    Stars(random.randrange(40, 60))
    
    # Menu Options
    
    global moodOne
    global moodTwo
    global moodThree
    global moodFour
    global info
    global settings
    
    title = Text((int(windowWidth/2), int(3 * windowHeight / 8)), (255, 255, 255), int(windowHeight/7), 'Mood Aesthetics')
    
    moodOne = Text((int(25 * windowWidth / 100), int(5 * windowHeight/9)), (255, 255, 255), int(windowHeight/24), 'Angry')
    
    moodTwo = Text((int(125/3 * windowWidth / 100), int(5 * windowHeight/9)), (255, 255, 255), int(windowHeight/24), 'Happy')
    
    moodThree = Text((int(175/3 * windowWidth / 100), int(5 * windowHeight/9)), (255, 255, 255), int(windowHeight/24), 'Sad')

    moodFour = Text((int(75 * windowWidth / 100), int(5 * windowHeight/9)), (255, 255, 255), int(windowHeight/24), 'Chill')
    
    title.draw()
    moodOne.draw()
    moodTwo.draw()
    moodThree.draw()
    moodFour.draw()
    
    # Info Button
    info = Text((int(windowWidth/20), int(19 * windowHeight / 20)), (255, 255, 255), int(windowHeight/35), 'about')
    settings = Text((int(18.5 * windowWidth/20), int(19 * windowHeight / 20)), (255, 255, 255), int(windowHeight/35), 'settings')
    info.draw()
    settings.draw()
    
def drawButtons():
    
    global settings
    global title
    global about
    global quit
    
    title = Text((int(windowWidth/2), int(3 * windowHeight / 9)), (255, 255, 255), int(windowHeight/5), 'Paused')

    settings = Text((int(windowWidth/2), int(5 * windowHeight / 9)), (255, 255, 255), int(windowHeight/25), 'Settings')
    about = Text((int(windowWidth/2), int(6 * windowHeight / 9)), (255, 255, 255), int(windowHeight/25), 'About')
    quit = Text((int(windowWidth/2), int(7 * windowHeight / 9)), (255, 255, 255), int(windowHeight/25), 'Quit')
    
    title.draw()
    settings.draw()
    about.draw()
    quit.draw()

class Text:
    def __init__(self, centerPoint, color, height, text):
        height = int(height * 1.2)
        self.actualtext = text
        self.font = pg.font.Font('Fonts/proximanova.ttf', height)
        text = self.font.render(text, 1, color)
        textRect = text.get_rect()
        textRect.center = centerPoint
        self.rectangle = textRect
        self.text = text
        
    def draw(self):    
        screen.blit(self.text, self.rectangle)
        titles.append(self.rectangle)
        
    def getRectangle(self):
        return self.rectangle  
    
    def getText(self):
        return self.actualtext      
    
class Stars:
    def __init__(self, number): 
        stars = []
        for i in range(number):
            xPoint = random.randrange(6, windowWidth - 5)
            yPoint = random.randrange(6, windowHeight - 5)
            if windowWidth >= 160:
                radius = random.randrange(1, int(windowWidth/160))
            else:
                radius = 1
            star = pg.draw.circle(screen, (255, 255, 255), [xPoint, yPoint], radius)
            stars.append(star)
            
class underLine:
    def __init__(self, rectangle):
        x1 = rectangle.centerx - rectangle.width/2
        x2 = rectangle.centerx + rectangle.width/2
        y = rectangle.centery + rectangle.height/2
        pg.draw.line(screen, (255, 255, 255), (x1, y), (x2, y), 1)

def aboutMenu():
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        if event.type == KEYDOWN and event.key == pg.K_ESCAPE:
            Variables.about = False
            Variables.escape = False
            Variables.settingsmenu = False
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            Variables.about = False
            Variables.escape = False
            Variables.settingsmenu = False
    screen.fill(pg.Color('Black'))
    Stars(random.randrange(40, 60))
    
    aboutTitle = Text((int(windowWidth/2), int(1.6 * windowHeight / 8)), (255, 255, 255), int(windowHeight/5), 'About')    
    quote1 = Text((int(windowWidth/2), int(3.1 * windowHeight / 8)), (235,13,190), int(windowHeight/28), "Sometimes a musical phrase")
    quote2 = Text((int(windowWidth/2), int(3.5 * windowHeight / 8)), (235,13,190), int(windowHeight/28), "would perfectly sum up the mood of a moment.")
    quote3 = Text((int(3 * windowWidth / 5), int(4.1 * windowHeight / 8)), (235,13,190), int(windowHeight/28), "-John Ashberry")
    body1 = Text((int(windowWidth / 2), int(5.1 * windowHeight / 8)), (255, 255, 255), int(windowHeight/35), "Mood Aesthetics is an interactive computer program centered around")
    body2 = Text((int(windowWidth / 2), int(5.5 * windowHeight / 8)), (255, 255, 255), int(windowHeight/35), "four basic human emotions: anger, sadness,happiness ,and tranquility.")
    body3 = Text((int(windowWidth / 2), int(5.9 * windowHeight / 8)), (255, 255, 255), int(windowHeight/35), "It displays graphic animations with matching sonic melodies which")
    body4 = Text((int(windowWidth / 2), int(6.3 * windowHeight / 8)), (255, 255, 255), int(windowHeight/35), "correspond with the mood chosen by the user. Mood Aesthetics' goal")
    body5 = Text((int(windowWidth / 2), int(6.7 * windowHeight / 8)), (255, 255, 255), int(windowHeight/35), "is to enhance the user's present mood by finding the perfect")
    body6 = Text((int(windowWidth / 2), int(7.1  * windowHeight / 8)), (255, 255, 255), int(windowHeight/35), "blend of sound, animation, and emotion.")
    instructions = Text((int(windowWidth/2), int(38 * windowHeight/40)), (255, 255, 255), int(windowHeight/50), 'Press Escape to Return')
    instructions.draw()
    
    quote1.draw()
    quote2.draw()
    quote3.draw() 
    body1.draw()
    body2.draw()
    body3.draw()
    body4.draw() 
    body5.draw()
    body6.draw()
    aboutTitle.draw()
    
    pg.display.flip()
    pg.time.Clock().tick(int(bpm/3))     

def settingsMenu():
    mouse = pg.mouse.get_pos()
            
    screen.fill(pg.Color('Black'))
    Stars(random.randrange(40, 60))                
    
    title = Text((int(windowWidth/2), int(3 * windowHeight / 9)), (255, 255, 255), int(windowHeight/5), 'Volume')
    title.draw()
    
    instructions = Text((int(windowWidth/2), int(38 * windowHeight/40)), (255, 255, 255), int(windowHeight/50), 'Press Escape to Return')
    instructions.draw()
    
    volumes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    volumebuttons = []
    
    for volume in volumes:
        if volume == Variables.currentVolume:
            volumebutton = Text((int(windowWidth/2 + (volume - 5) * windowWidth/25), int(5 * windowHeight / 9)), (0, 0, 0), int(windowHeight/30), str(volume))
            rectangle = volumebutton.getRectangle()
            pg.draw.rect(screen, (255, 255, 255), rectangle)
            volumebutton.draw()
        else:
            volumebutton = Text((int(windowWidth/2 + (volume - 5) * windowWidth/25), int(5 * windowHeight / 9)), (255, 255, 255), int(windowHeight/30), str(volume))
            volumebutton.draw()
        volumebuttons.append(volumebutton)
            
    
    for volumebutton in volumebuttons:
        if volumebutton.getRectangle().collidepoint(mouse):
            underLine(volumebutton.getRectangle())
            
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == pg.K_ESCAPE:
                Variables.about = False
                Variables.escape = False
                Variables.settingsmenu = False
                return
            elif event.key == K_LEFT and Variables.currentVolume > 0:
                Variables.currentVolume = Variables.currentVolume - 1
            elif event.key == K_RIGHT and Variables.currentVolume < 10:
                Variables.currentVolume = Variables.currentVolume +  1
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            for volumebutton in volumebuttons:
                if volumebutton.getRectangle().collidepoint(mouse):
                    Variables.currentVolume = int(volumebutton.getText())
            
    
    pg.mixer.music.set_volume(Variables.currentVolume * .1)
                            
    pg.display.flip()
    pg.time.Clock().tick(int(bpm/3))
          
def escapeMenu():
    mouse = pg.mouse.get_pos()
    for event in pg.event.get():
        global escape
        global about
        if event.type == QUIT:
            pg.quit()
            exit()
        if event.type == KEYDOWN and event.key == pg.K_ESCAPE:
            Variables.about = False
            Variables.escape = False
            return
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if settings.getRectangle().collidepoint(mouse):
                Variables.settingsmenu = True
                Variables.escape = False
                Variables.about = False
                return
            elif about.getRectangle().collidepoint(mouse):
                Variables.about = True
                Variables.escape = False
                Variables.settingsmenu = False
                return
            elif quit.getRectangle().collidepoint(mouse):
                pg.quit()
                exit()
            else:
                Variables.escape = False
            
    screen.fill(pg.Color('Black'))
    Stars(random.randrange(40, 60)) 
    instructions = Text((int(windowWidth/2), int(38 * windowHeight/40)), (255, 255, 255), int(windowHeight/50), 'Press Escape to Return')
    instructions.draw()               
    drawButtons()
            
    if settings.getRectangle().collidepoint(mouse):
        underLine(settings.getRectangle())
    elif about.getRectangle().collidepoint(mouse):
        underLine(about.getRectangle())
    elif quit.getRectangle().collidepoint(mouse):
        underLine(quit.getRectangle())
                    
                        
    pg.display.flip()
    pg.time.Clock().tick(int(bpm/3))     

def main():
    
    global bpm
    pg.mixer.music.load(Songs[0][0])
    bpm = Songs[0][1]
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(Variables.currentVolume * .1)

    while True:
        menu()
        for event in pg.event.get():
            if event.type == QUIT:
                    pg.quit()
                    exit()
            
            if event.type == KEYDOWN and event.key == pg.K_ESCAPE:
                    Variables.escape = True
            
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                
                mouse = pg.mouse.get_pos()
                musicStopTime = pg.mixer.music.get_pos()
                
                if moodOne.getRectangle().collidepoint(mouse):
                    Angry.main()
                    Polygons.main()
                    pg.mixer.music.load(Songs[0][0])
                    bpm = Songs[0][1]
                    pg.mixer.music.play(-1, musicStopTime / 1000)
                elif moodTwo.getRectangle().collidepoint(mouse): 
                    Happy.main()
                    pg.mixer.music.load(Songs[0][0])
                    bpm = Songs[0][1]
                    pg.mixer.music.play(-1, musicStopTime / 1000)
                elif moodThree.getRectangle().collidepoint(mouse):
                    Sad.main()
                    pg.mixer.music.load(Songs[0][0])
                    bpm = Songs[0][1]
                    pg.mixer.music.play(-1, musicStopTime / 1000)
                elif moodFour.getRectangle().collidepoint(mouse):
                    Chill.main()
                    pg.mixer.music.load(Songs[0][0])
                    bpm = Songs[0][1]
                    pg.mixer.music.play(-1, musicStopTime / 1000)
                    
                elif info.getRectangle().collidepoint(mouse):
                    Variables.about = True
                elif settings.getRectangle().collidepoint(mouse):
                    Variables.settingsmenu = True
            pg.mixer.music.set_volume(Variables.currentVolume * .1)

        mouse = pg.mouse.get_pos()
        if moodOne.getRectangle().collidepoint(mouse):
            underLine(moodOne.getRectangle())
        elif moodTwo.getRectangle().collidepoint(mouse):
            underLine(moodTwo.getRectangle())
        elif moodThree.getRectangle().collidepoint(mouse):
            underLine(moodThree.getRectangle())
        elif moodFour.getRectangle().collidepoint(mouse):
            underLine(moodFour.getRectangle())
        elif info.getRectangle().collidepoint(mouse):
            underLine(info.getRectangle())
        elif settings.getRectangle().collidepoint(mouse):
            underLine(settings.getRectangle())
                                    
        pg.display.flip()
        pg.time.Clock().tick(int(bpm/3)) 
        while Variables.escape == True:
            escapeMenu()
        while Variables.about == True:
            aboutMenu()  
        while Variables.settingsmenu == True:
            settingsMenu()     
if __name__ == "__main__":    
    main()   
