import pygame
import time
import random

pygame.init()
##Initializes screen, sets size, caption, timer, font, and colors.
##Also creates variables for white and black.
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Yahtzee")
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 18)
background = (128, 128, 128)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)
red = (200, 0, 0)
numbers = [0, 0, 0, 0, 0,]
roll = False

	#(left, up, width, height)
leftAlign = WIDTH/2 - 50
topOne = 300
middleOne = 450
bottomOne = 600
buttonWidth = 100
buttonHeight = 50

smallText = pygame.font.Font("freesansbold.ttf",20)
midText = pygame.font.Font('freesansbold.ttf', 50)
largeText = pygame.font.Font('freesansbold.ttf',115)

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action == "Play":
               game_loop()
            elif action == "Rules":
               rules_page()
            elif action == "Back":
               game_intro()
            elif action == "Quit":
               pygame.quit()
               quit()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def rules_page():
    screen.fill(background)

    TextSurf, TextRect = text_objects("The Rules of", midText)
    TextRect.center = ((WIDTH/2), (HEIGHT/8))
    screen.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_objects("YAHTZEE", largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/4))
    screen.blit(TextSurf, TextRect)
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()

        Back = button("Back", leftAlign, middleOne, buttonWidth, buttonHeight, black, green, "Back")
        Quit = button("Exit", leftAlign, bottomOne, buttonWidth, buttonHeight, black, red, "Quit")

        pygame.display.update()
        timer.tick(15)

def game_loop():
    print("Hello")

def game_intro():
    intro = True
    screen.fill(background)

    TextSurf, TextRect = text_objects("YAHTZEE", largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/4))
    screen.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_objects("Welcome to", midText)
    TextRect.center = ((WIDTH/2), (HEIGHT/8))
    screen.blit(TextSurf, TextRect)

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()

        Rules = button("Rules", leftAlign, topOne, buttonWidth, buttonHeight, black, green, "Rules")
        Play = button("Play", leftAlign, middleOne, buttonWidth, buttonHeight, black, green, "Play")
        Quit = button("Exit", leftAlign, bottomOne, buttonWidth, buttonHeight, black, red, "Quit")

        pygame.display.update()
        timer.tick(15)

game_intro()
pygame.quit()
quit()
