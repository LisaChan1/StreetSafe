import pygame, sys
from pygame.locals import *
import random
import math
import time

# initializing pygame
pygame.init()

# creating game screen
screen = pygame.display.set_mode([1425, 800])

# Title & icon
pygame.display.set_caption("StreetSafe")
icon = pygame.image.load('city-2.png')
pygame.display.set_icon(icon)

#fonts
mmfont = pygame.font.SysFont(None, 70)
mfont = pygame.font.SysFont(None, 100)
font = pygame.font.Font('freesansbold.ttf', 32)
font1 = pygame.font.Font('freesansbold.ttf', 20)




def display_score(xpos, ypos, scoreVal):
    score = font.render('Score: ' + str(scoreVal), True, (255, 255, 255))
    screen.blit(score, (xpos, ypos))


#DRAWING ALL CHARACTERS TO SCREEN
#drawing player to screen
def player(x, y, playerImg):
    screen.blit(playerImg, (x, y))


#drawing enemy to screen
def enemy(x, y, enemyImg):
    screen.blit(enemyImg, (x, y))


def distance(objX1, objY1, objX2, objY2):
    dist = math.sqrt(math.pow(objX2 - objX1, 2) + math.pow(objY2 - objY1, 2))
    return dist


#making object 2 move towards object 1 (in one direction)
def moveTowards(pos1, pos2, change, interval):
    if (pos1 < pos2):
        change = -interval
    elif (pos1 > pos2):
        change = interval
    return change




#drawing goose dialogue to screen
def dialogue(x, y, dialogueImg):
    screen.blit(dialogueImg, (x, y))

def display_options(xpos, ypos, text):
    display_text(text, font, (255, 255, 255), screen, xpos, ypos)

def display_text(txt, font, colour, screen, xpos, ypos):
    text = font.render(txt, True, colour)
    #txtrec = txtobj.get_rect()
    #txtrec.topleft = (xpos, ypos)
    screen.blit(text, (xpos, ypos))

class Button:
    def __init__(self, pos):
        self.rect = pygame.Rect(pos)

def on_click(self, event):
    if event.button == 1:
        if self.rect.collidepoint(event.pos):
            self.callback(self)

#main menu screen
def main_menu():
    running = True
    while running:
        click = False
        screen.fill((0, 0, 0))
        display_text('STREETSAFE', mfont, (255, 255, 255), screen, 490, 200)
        display_text('MENU', mmfont, (255, 255, 255), screen, 630, 300)
        #mousex, mousey = pygame.mouse.get_pos()
        button1 = Button((605, 400, 210, 50))
        button2 = Button((605, 500, 210, 50))
        button3 = Button((605, 600, 210, 50))

        pygame.draw.rect(screen, (255,0,0), button1)
        pygame.draw.rect(screen, (255,0,0), button2)
        pygame.draw.rect(screen, (255,0,0), button3)
        

       # if button1.collidepoint(mousex, mousey):
            #if click:
                #level_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                #sys.exit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if event.key == pygame.K_1:
                if button1.rect.collidepoint(pygame.mouse.get_pos()):
                #if event.button == 1:
                    #if button1.rect.collidepoint(pygame.mouse.get_pos()):
                        
                #if event.button == 1:
                    #click = True
                    episode1()
        #if button3.collidepoint(mousex, mousey):
        #if click:
            #resources()
        pygame.draw.rect(screen, (255,0,0),button1)
        pygame.draw.rect(screen, (255,0,0),button2)
        pygame.draw.rect(screen, (255,0,0),button3)

        display_text('PLAY GAME', font, (255,255,255), screen, 612, 410)
        display_text('CHAT NOW', font, (255,255,255), screen, 620, 510)
        display_text('RESOURCES', font, (255,255,255), screen, 609, 610)
        #click = False
        
        pygame.display.update()

def level_menu():
    running = False
    while running:
        click = False
        screen.fill((0, 0, 0))
        display_text('Episodes', font, (255, 255, 255), screen, 250, 300)
        mousex, mousey = pygame.mouse.get_pos()
        button1 = pygame.Rect(200, 100, 200, 50)
        button2 = pygame.Rect(200, 180, 200, 50)
        button3 = pygame.Rect(200, 260, 200, 50)

        if button1.collidepoint(mousex, mousey):
            if click:
                episode1()
        pygame.draw.rect(screen, (255,0,0),button1)
        pygame.draw.rect(screen, (255,0,0),button2)
        pygame.draw.rect(screen, (255,0,0),button3)

        display_text('Episode 1', font, (255,255,255), screen, 270, 115)
        display_text('Episode 2', font, (255,255,255), screen, 250, 195)
        display_text('Episode 3', font, (255,255,255), screen, 270, 215)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                #sys.exit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()

def episode1():
    #background
    bg = pygame.image.load("background.png")

    #PLAYER SETUP
    playerImg = pygame.image.load('Main_sideview.png')
    playerX = 25
    playerY = 500
    move = 3
    changeX = 0
    changeY = 0

    #ENEMY SETUP
    enemyImg = pygame.image.load('villan.png')
    enemyX = random.randint(300, 1200)
    enemyY = random.randint(300, 600)
    enemyMove = 3
    enemyChangeX = random.randint(-3, 3)
    enemyChangeY = random.randint(-2, 3)
    eMoveList = [-2, -1, 1, 2]

    
    #dialogue1 = 'A strange encounter. What should you do?'
    #dialogue2 = 'Ignore the remark and keep walking OR Call it out'
    #score
    scoreVal = 0
    textposX = 10
    textposY = 10

    # game loop
    running = True
    while running:
        #creating background
        screen.fill((4, 7, 36))
        screen.blit(bg, (0, 0))

        #checking if user presses arrow key/quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # checking whether arrow keys pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    changeX -= move
                if event.key == pygame.K_RIGHT:
                    changeX += move
                if event.key == pygame.K_UP:
                    changeY -= move
                if event.key == pygame.K_DOWN:
                    changeY += move
            # checking if arrow key no longer being pressed (stops movement)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    changeX = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeY = 0
        #adjusting player's x and y position
        playerX += changeX
        playerY += changeY

        #checking if player moved out of bounds
        if playerY >= 600:
            playerY = 600
        elif playerY <= 300:
            playerY = 300
        if playerX <= 0:
            playerX = 0
        elif playerX >= 1200:
            playerX = 1200

        #adjusting enemy's x and y position
        enemyX += enemyChangeX
        enemyY += enemyChangeY

        #checking if enemy moved out of bounds
        if enemyY >= 600:
            enemyY = 600
            enemyChangeY -= enemyMove
            enemyChangeX = random.choice(eMoveList)
            enemyChangeY = random.choice(eMoveList)
        elif enemyY <= 300:
            enemyY = 300
            enemyChangeY += enemyMove
            enemyChangeX = random.choice(eMoveList)
            enemyChangeY = random.choice(eMoveList)
        if enemyX <= 0:
            enemyX = 0
            enemyChangeX += enemyMove
            enemyChangeX = random.choice(eMoveList)
            enemyChangeY = random.choice(eMoveList)
        elif enemyX >= 1200:
            enemyX = 1200
            enemyChangeX -= enemyMove
            enemyChangeX = random.choice(eMoveList)
            enemyChangeY = random.choice(eMoveList)

        #checking if the player and enemy collided
        dist = distance(playerX, playerY, enemyX, enemyY)
        if (dist < 75):
            enemyChangeX = 0
            enemyChangeY = 0
            changeX = 0
            changeY = 0
            interaction()
            running = False
        else:
            if (dist < 200):
                #initiate catcalling
                enemyChangeX = moveTowards(playerX, enemyX, enemyChangeX, enemyMove)
                enemyChangeY = moveTowards(playerY, enemyY, enemyChangeY, enemyMove)

            #drawing enemy and player to the screen
            player(playerX, playerY, playerImg)
            display_score(textposX, textposY, scoreVal)
            enemy(enemyX, enemyY, enemyImg)

        #updating the display
    #pygame.display.update()
        pygame.display.flip()

def interaction():
    #bg = pygame.image.load("black_screen.png")
    #

    #DIALOGUE SETUP
    dialogueImg = pygame.image.load('speech_bubble.png')
    dialogueX = 400
    dialogueY = 100
    running = True
    response = 0
    while running:
        #screen.fill((0, 0, 0))
        #screen.blit(bg, (0, 0))
        
        screen.blit(dialogueImg, (dialogueX,dialogueY))
        #display_options(dialogueX,dialogueY, dialogue1)
        #display_options(dialogueX,dialogueY, dialogue2)
        display_text("A strange encounter. What should you do? ", font1, (0,0,0), screen, dialogueX+100,dialogueY+300)
        display_text("Press the corresponding letter on your keyboard to select a choice", font1, (0,0,0), screen, dialogueX+100,dialogueY+400)
        display_text("Ignore the remark(A) and keep walking OR Call it out(B)", font1, (0,0,0), screen, dialogueX+100,dialogueY+500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    response = 1
                if event.key == pygame.K_b:
                    response = 2
                    
        if response == 1:
            display_text("You missed it! Good job ignoring that remark!", font1, (0,0,0), screen, dialogueX+100,dialogueY+600)
            display_text("The end! Press the red X to quit", font1, (0,0,0), screen, dialogueX+100,dialogueY+700)
            #running = False
        elif response == 2:
            display_text("You made it! You just experienced street harrassment!", font1, (0,0,0), screen, dialogueX+100,dialogueY+600)
            display_text("The end! Press the red X to quit", font1, (0,0,0), screen, dialogueX+100,dialogueY+700)
            #running = False
            
        pygame.display.update()

main_menu()
