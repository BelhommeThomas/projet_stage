#inport moduel
import pygame
import random
import time
from tkinter import *
#initialise pygame

#colors
white = (255,255,255)
black = (0,0,0)
gbgreenlg = (155, 188, 15)
gbgreendk = (15, 56, 15)
crystal = (104, 160, 176)
rock = (128, 132, 135)
waky_snek = ((round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10))
waky_background = ((round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10))
waky_fruit =((round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10))
#window
win_width = 600
win_height = 400
def start_pygame(snek_lvl):
    global win
    global fps
    pygame.init()
    win = pygame.display.set_mode((win_width,win_height))
    pygame.display.set_caption('snek lvl ' + snek_lvl)
    fps = pygame.time.Clock()

#def
def snek(snek_list, snek_color):
    for x in snek_list:
        pygame.draw.rect(win, snek_color, [x[0], x[1], 10, 10])

def gameLoop1(snek_speed,color_palette_background, color_palette_snek):
    #base values
    global waky_background
    global waky_snek
    x1 = win_width/2
    y1 = win_height/2
    x1_change = 0
    y1_change = 0
    gameover = False
    snek_length = 1
    snek_list = []
    waky_snek = ((round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10))
    waky_fruit =((round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10))
    waky_background = ((round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10))
    snek_color = color_palette_snek
    fruitx = round(random.randrange(10,500)/10.0)*10.0
    fruity = round(random.randrange(10,300)/10.0)*10.0
    if snek_speed == 1:
        increase = True
        snek_speed = 5
    else:
        increase = False
    while not gameover:
        win.fill(color_palette_background)
        for event in pygame.event.get():
            #exit via X
            if event.type == pygame.QUIT:
                gameover = True
            #controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10
        #movement
        x1 += x1_change
        y1 += y1_change
        
        #make snek grow
        snek_head = []
        snek_head.append(x1)
        snek_head.append(y1)
        snek_list.append(snek_head)
        if len(snek_list) > snek_length:
            del snek_list[0]
        for x in snek_list[:-1]:
            if x == snek_head:
                gameover = True
        
        #draw movement
        snek(snek_list, snek_color)
        pygame.draw.rect(win, waky_fruit, [fruitx, fruity, 10, 10])
        pygame.display.update()

        
        #thing that doesn't make it sanic
        fps.tick(snek_speed)
        #gameover condition
        if x1 >= win_width + 1 or x1 <= -1 or y1 >= win_height + 1 or y1 <= -1:
            gameover = True
        #it should make the fucking fruit but fuck me I guess, never mind I fixed the fucker
        if fruitx == x1 and fruity == y1:
            fruitx = round(random.randrange(10,500)/10.0)*10.0
            fruity = round(random.randrange(10,300)/10.0)*10.0
            if increase == True:
                snek_speed += 1 
                waky_fruit =((round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10),(round(random.randrange(1,255)/10)*10))
                pygame.draw.rect(win, waky_fruit, [fruitx, fruity, 10, 10])
            else:
                pygame.draw.rect(win, black, [fruitx, fruity, 10, 10])
            snek_length += 1 
                    
    pygame.quit()

def but():
    start_pygame('1')
    gameLoop1(5,white,black)
def butt():
    start_pygame('2')
    gameLoop1(10,gbgreenlg,gbgreendk)
def buttt():
    start_pygame('3')
    gameLoop1(15,rock,crystal)
def butttt():
    start_pygame('increasing')
    gameLoop1(1,waky_background,waky_snek)

snk = Tk()
snk.title('snek menu!')

#window size
snk.minsize(500,500)
snk.maxsize(500,500)
#buttons
button_lvl_1 = Button(snk, text='level 1', padx = 10, pady = 10, command=but)
button_lvl_2 = Button(snk, text='level 2', padx = 10, pady = 10, command=butt)
button_lvl_3 = Button(snk, text='level 3', padx = 10, pady = 10, command=buttt)
button_lvl_increasing = Button(snk, text='level increasing', padx = 10, pady = 10, command=butttt)
button_lvl_1.grid(row = 0, column=1)
button_lvl_2.grid(row = 0, column=2)
button_lvl_3.grid(row = 0, column=3)
button_lvl_increasing.grid(row = 0, column=0)

snk.mainloop()