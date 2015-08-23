import pygame, random
from pygame.locals import *
from sys import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN=(85,107,47)
L_GREEN=(45, 51, 22)
YELLOW=(255, 250, 0)


pygame.init()
l, b=700, 480
c,c2=7.5, 42.0      #constants for Player bars boundaries
sp= 250.
flag=0

screen=pygame.display.set_mode((l, b),0,32)
pygame.display.set_caption("My Pong")

#Creating 2 bars, a ball and background.
back = pygame.Surface((l,b))
background = back.convert()
background.fill(WHITE)
bar = pygame.Surface((10,50))
bar1 = bar.convert()
bar1.fill((0,0,255))
bar2 = bar.convert()
bar2.fill((255,0,0))
circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(0,255,0),(7,7),7)
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

# some definitions
bar1_x, bar2_x = 10. , l-20
bar1_y, bar2_y = 215. , 215.
circle_x, circle_y = random.randrange(300,350), random.randrange(200,250)
bar1_move, bar2_move = 0. , 0.
speed_x, speed_y = sp,sp
speed_circ =sp


#Text on Screen
def text_to_screen(screen, text, x,y, size):
    text=str(text)
    font =pygame.font.SysFont("comicsansms",size)
    text=font.render(text, True, BLACK)
    screen.blit(text, (x,y))

    

bar1_score, bar2_score = 0,0
#clock and font objects
clock = pygame.time.Clock()
 

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                bar1_move = -ai_speed
            elif event.key == K_DOWN:
                bar1_move = ai_speed
        elif event.type == KEYUP:
            if event.key == K_UP:
                bar1_move = 0.
            elif event.key == K_DOWN:
                bar1_move = 0.

    #BACKGROUND Court Frame
     
    screen.blit(background,(0,0))
    frame = pygame.draw.rect(screen,BLACK,Rect((5,5),(l-10,b-10)),2)
    middle_line = pygame.draw.aaline(screen,BLACK,(l/2-10,5),(l/2-10,475))
    pygame.draw.circle(screen,BLACK,(10,int(b/2)),int(b/2),0)   #left court semicircle
    pygame.draw.circle(screen,BLACK,(l-10,int(b/2)),int(b/2),0) #right court semicircle
  #  pygame.draw.circle(screen,BLACK,(int(l/2),int(b/2)),100,2)
    
    screen.blit(bar1,(bar1_x,bar1_y))
    screen.blit(bar2,(bar2_x,bar2_y))
    screen.blit(circle,(circle_x,circle_y))
    text_to_screen(screen, bar1_score, 250, 5, 50)
    text_to_screen(screen, bar2_score, 380, 5, 50)
     

    bar1_y += bar1_move
    
# movement of circle    *****
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0
    
    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec
    ai_speed = speed_circ * time_sec    ##ai

    
#AI of the computer.
    if circle_x >= 333.0:
        if not bar2_y == circle_y + c:
            
            if bar2_y < circle_y + c:           #If player2 is much above
                bar2_y += ai_speed
            if  bar2_y > circle_y - c:       #If player2 is much below
                bar2_y -= ai_speed
        else:
            bar2_y == circle_y + c      #If P2 y_coord in close proximity, strike ball being somewhere in the middle

    #Players WITHIN the Boundary Confinement.
    if bar1_y >= b-60.0: bar1_y = b-60.0
    elif bar1_y <= 10. : bar1_y = 10.
    if bar2_y >= b-60.: bar2_y = b-60.0
    elif bar2_y <= 10.: bar2_y = 10.


#Hitting logic
    if circle_x <= bar1_x + 10.:                #Ball aligned with P1
        
        if circle_y >= bar1_y - c and circle_y <= bar1_y + c2:
            circle_x = 20.
            speed_x = -speed_x
    if circle_x >= bar2_x - 15.:
        if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
            circle_x = 605.
            speed_x = -speed_x
    if circle_x < 5.:
        bar2_score += 1
        circle_x, circle_y = random.randrange(300,350), random.randrange(200,250)  #Reallotment of ball pos
        bar1_y,bar_2_y = 215., 215.
    elif circle_x > l-20.:      #P2 Loses
        bar1_score += 1
        circle_x, circle_y =  random.randrange(300,350), random.randrange(200,250)  #Reallotment
        bar1_y, bar2_y = 215., 215.
        
    if circle_y <= 10.:     #Upper wall Reflection
        speed_y = -speed_y
        circle_y = 10.
    elif circle_y >=b-22.0: #Lower wall reflection
        speed_y = -speed_y
        circle_y = b-22.0

    if bar1_score==5:
        flag=1
         
        bar1_score, bar2_score=0,0
    if bar2_score==5 :
        flag=2
        
        bar1_score, bar2_score=0,0
     

    pygame.display.update()
