'''
Created on Jul 22, 2013

@author: catapult
'''
'''
Created on Jul 18, 2013

@author: catapult
'''


import zellegraphics as zg

import time
import random
import math
import pygame as pg
import Menu 

def main():
    pg.init()
    pg.mixer.init()
    
    windowWidth = Menu.windowWidth
    windowHeight = Menu.windowHeight
    
    pg.mixer.music.load(Menu.Songs[4][0])
    pg.mixer.music.play(0)
    screen = pg.display.set_mode([10,10])
    
    win=zg.GraphWin(width=windowWidth, height=windowHeight)
    
    windowWidth=1000
    windowHeight=600
    
    
    background = zg.Rectangle(zg.Point(-10, -10), zg.Point(windowWidth+10, windowHeight+10))
    background.setFill("Black")
    background.draw(win)
    bps=.175
    
    #colors
    chillColors = [zg.color_rgb(251, 202, 134), zg.color_rgb(222, 235, 220), zg.color_rgb(154, 212, 239), zg.color_rgb(207, 216, 220), 
                   zg.color_rgb(65, 73, 76), zg.color_rgb(161, 152, 146),zg.color_rgb(152, 32, 108), zg.color_rgb(202, 75, 160)]
    
    
    def randomColor(colors):
        
        i=random.randrange(0, len(chillColors))
        color=colors[i]
        return color
        
    #Triangle 1 
    def equilateralTriangle(lowerLeftPoint, width, colors):
        x1=lowerLeftPoint.getX()
        y1=lowerLeftPoint.getY()
        x2=x1+width
        y2=y1
        x3=x1+width/2
        y3=y1-width*math.sqrt(3)/2
        points= [zg.Point(x1,y1), zg.Point(x2,y2), zg.Point(x3,y3)]
        triangle=zg.Polygon(points)
        triColor = randomColor(chillColors)
        triangle.setOutline(triColor)
        triangle.setFill(triColor)
        triangle.draw(win)
    
    def triN(n, lowerLeftPoint, width,colors):
        if n <=1:
            equilateralTriangle(lowerLeftPoint, width,colors)
        else:    
            triN(n-1, lowerLeftPoint, width/2,colors)
            triN(n-1, zg.Point(lowerLeftPoint.getX()+ width/2, lowerLeftPoint.getY()), width/2,colors)
            triN(n-1, zg.Point (lowerLeftPoint.getX()+width/4, lowerLeftPoint.getY()-math.sqrt(3)/2*width/2),width/2,colors)
        
    
    
    
    #Triangle 2   
    def equilateralTriangle2(upperRightPoint, width, colors):
        x1=upperRightPoint.getX()
        y1=upperRightPoint.getY()
        x2=x1-width
        y2=y1
        x3=x1-width/2
        y3=y1+width*math.sqrt(3)/2
        
    
        points= [zg.Point(x1,y1), zg.Point(x2,y2), zg.Point(x3,y3)]
        triangle=zg.Polygon(points)
        triColor = randomColor(chillColors)
        triangle.setOutline(triColor)
        triangle.setFill(triColor)
        triangle.draw(win)
    
    def triN2(n, upperRightPoint, width, colors):
        if n <=1:
            equilateralTriangle2(upperRightPoint, width, colors)
        else:    
            triN2(n-1,upperRightPoint, width/2, colors)
            triN2(n-1, zg.Point(upperRightPoint.getX()-width/2, upperRightPoint.getY()), width/2,colors)
            triN2(n-1, zg.Point (upperRightPoint.getX()-width/4, upperRightPoint.getY()+math.sqrt(3)/2*width/2),width/2,colors)
    #tri spread
    def equilateralTriangleN3(lowerLeftPoint, width, color):
        x1=lowerLeftPoint.getX()
        y1=lowerLeftPoint.getY()
        x2=x1+width
        y2=y1
        x3=x1+width/2
        y3=y1-width*math.sqrt(3)/2
        #newtri
        lowerLeftPoint2= zg.Point(lowerLeftPoint.getX()+width/2+10,lowerLeftPoint.getY()-math.sqrt(3))
        x4= x2 + 10
        y4=y1
        x5=x3 + 10
        y5 = y3
        x6 =x5+width
        y6 = y5
        points= [zg.Point(x4,y4), zg.Point(x5,y5), zg.Point(x6,y6)]
        triangle=zg.Polygon(points)
        triColor = randomColor(chillColors)
        triangle.setOutline(triColor)
        triangle.setFill(triColor)
        triangle.draw(win)
    
    def triN3(n, lowerLeftPoint2, width, colors):
        if n <=1:
            equilateralTriangleN3(lowerLeftPoint2, width, colors)
        else:    
            triN3(n-1,lowerLeftPoint2, width/2, colors)
            triN3(n-1, zg.Point(lowerLeftPoint2.getX()+ width/2, lowerLeftPoint2.getY()), width/2, colors)
            triN3(n-1, zg.Point (lowerLeftPoint2.getX()+width/4, lowerLeftPoint2.getY()+math.sqrt(3)/2*width/2),width/2, colors)
    
    
    
    
    edge = int(windowWidth / (6 + 2/3))
    width = windowWidth * .3
    x1 = edge + width
    x2 = windowWidth * .5 - width * .5
    x3 = windowWidth - edge
    y1 = windowHeight * .5 - .25 * width * math.sqrt(3)
    y2 = windowHeight * .5 + .25 * width * math.sqrt(3) 
    y3 = windowHeight * .5 - .25 * width * math.sqrt(3) 
    
    
    
    #Triangles Draw
    "insert shape, then put a background fill between each shape if you want background to always flash, then time sleep for bpm"
    
    
    
    for i in range (9):
        triN2(i+1,zg.Point(1000, 0), 11000, chillColors)
        background.setFill(randomColor(chillColors))
        time.sleep(bps)
        
    for i in range (6):
        triN(i+1,zg.Point(x2, y2), 78000,chillColors)  
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(x3, y3), width, chillColors)
        triN2(i+1,zg.Point(x3, y3), 9854, chillColors)
        background.setFill(randomColor(chillColors))
        time.sleep(bps)
    
    for i in range (7):
        triN3(i+1,zg.Point(150,575), 600, chillColors)
        background.setFill(randomColor(chillColors))
        triN(i+1,zg.Point(x2, y2), 80000,chillColors)
        time.sleep(bps)    
    
    for i in range (7):
        triN(i+1,zg.Point(x2, y2), 8000,chillColors)
        background.setFill(randomColor(chillColors))
        time.sleep(bps)
    
    for i in range (5):
        triN2(i+1,zg.Point(x1, y1), width,chillColors)
        triN2(i+1,zg.Point(x3, y3), 985400, chillColors)
        background.setFill(randomColor(chillColors))
    
    for i in range (7):
        triN2(i+1,zg.Point(x1, y1), 11000,chillColors) 
        background.setFill(randomColor(chillColors))
        triN3(i+1,zg.Point(400,10), 400, chillColors)   
        time.sleep(bps)
        
    for i in range (5):
        triN(i+1,zg.Point(x2, y2), width,chillColors)
        background.setFill(randomColor(chillColors))
        triN(i+1,zg.Point(x2, y2), 900,chillColors)
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(1000, 0), 11000, chillColors)
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(x1, y1), 85760, chillColors)
        background.setFill(randomColor(chillColors))
        time.sleep(bps)
    
    for i in range (7):
        background.setFill(randomColor(chillColors))
        triN3(i+1,zg.Point(500,55), 900, chillColors)
        background.setFill(randomColor(chillColors))
        triN(i+1,zg.Point(x2, y2), 80000,chillColors)
        triN2(i+1,zg.Point(1000, 0), 11000, chillColors)
        background.setFill(randomColor(chillColors))
        triN(i+1,zg.Point(x2, y2), 1900,chillColors)
        background.setFill(randomColor(chillColors))
        time.sleep(bps)
    
    for i in range (4):
        background.setFill(randomColor(chillColors))
        triN(i+1,zg.Point(x2, y2), width,chillColors)
        background.setFill(randomColor(chillColors))
        triN(i+1,zg.Point(x2, y2), 900,chillColors)
        background.setFill(randomColor(chillColors))
        triN3(i+1,zg.Point(345,15), 400, chillColors)
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(x1, y1), 11000,chillColors) 
        background.setFill(randomColor(chillColors))
    
    for i in range (6):
        background.setFill
        triN2(i+1,zg.Point(1000, 0), 11000, chillColors)
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(x1, y1), 85760, chillColors)
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(x1, y1), 11000,chillColors) 
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(x3, y3), width, chillColors)
        triN2(i+1,zg.Point(x3, y3), 9854, chillColors)
        background.setFill(randomColor(chillColors))
        time.sleep(bps)
            
    for i in range (8):
        triN(i+1,zg.Point(x2, y2), 8000,chillColors)
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(x1, y1), 5000,chillColors)
        background.setFill(randomColor(chillColors))
    
    for i in range (4):
        triN3(i+1,zg.Point(150,575), 600, chillColors)
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(x1, y1), 85760, chillColors)
        background.setFill(randomColor(chillColors))
        triN3(i+1,zg.Point(500,55), 1000, chillColors)
        background.setFill(randomColor(chillColors))
        time.sleep(bps)
    
    for i in range (4):
        background.setFill(randomColor(chillColors))
        triN(i+1,zg.Point(x2, y2), width,chillColors)
        background.setFill(randomColor(chillColors))
        triN(i+1,zg.Point(x2, y2), 900,chillColors)
        background.setFill(randomColor(chillColors))
        triN3(i+1,zg.Point(345,15), 400, chillColors)
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(x1, y1), 11000,chillColors) 
        background.setFill(randomColor(chillColors))
    
    
    
    
    for i in range (6):
        background.setFill
        triN2(i+1,zg.Point(1000, 0), 11000, chillColors)
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(x1, y1), 85760, chillColors)
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(x1, y1), 11000,chillColors) 
        background.setFill(randomColor(chillColors))
        triN2(i+1,zg.Point(x3, y3), width, chillColors)
        triN2(i+1,zg.Point(x3, y3), 9854, chillColors)
        background.setFill(randomColor(chillColors))
        time.sleep(bps)    
    
    for i in range (7):
        triN3(i+1,zg.Point(150,575), 600, chillColors)
        background.setFill(randomColor(chillColors))
        triN(i+1,zg.Point(x2, y2), 80000,chillColors)
        time.sleep(bps)    
    
    for i in range (7):
        triN(i+1,zg.Point(x2, y2), 8000,chillColors)
        background.setFill(randomColor(chillColors))
        time.sleep(bps)
    
    for i in range (7):
        triN2(i+1,zg.Point(x1, y1), width,chillColors)
        triN2(i+1,zg.Point(x3, y3), 985400, chillColors)
        background.setFill(randomColor(chillColors))
        
        
    while True:
        background.setFill(randomColor(chillColors))
        time.sleep(bps)

    
    
if __name__ == "__main__":    
    main()    

