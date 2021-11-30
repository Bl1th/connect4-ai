import pygame
from pygame.locals import *
import os

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=700
screen_height=700
screen=pygame.display.set_mode((screen_width, screen_height))

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(75, 75, 75)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
darkblue=(28, 73, 102)
skyblue=(69, 182, 254)

# Game Fonts
font = "Montserrat-Bold.ttf"


# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    selected="start"
                elif event.key==pygame.K_s:
                    selected="setting"
                elif event.key==pygame.K_d:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        os.system('connect4_ai.py')
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(black)
        title=text_format("Connect-4", font, 90, skyblue)
        if selected=="start":
            text_start=text_format("START", font, 75, yellow)
        else:
            text_start = text_format("START", font, 75, gray)
        if selected=="setting":
            text_setting=text_format("SETTINGS", font, 75, yellow)
        else:
            text_setting = text_format("SETTINGS", font, 75, gray)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, yellow)
        else:
            text_quit = text_format("QUIT", font, 75, gray)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        setting_rect=text_setting.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_setting, (screen_width/2 - (setting_rect[2]/2), 360))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 420))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Connect 4")

#Initialize the Game
main_menu()
pygame.quit()
quit()
