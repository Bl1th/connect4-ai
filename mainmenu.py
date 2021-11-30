import pygame
from pygame.constants import QUIT
from pygame.locals import *
import os


# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=700
screen_height=700
screen=pygame.display.set_mode((screen_width, screen_height))

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

# Setting option
opsi_setting = "MINIMAX"

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

def mainmenu(opsi_setting):
    # Game Initialization
    pygame.init()

    class Option:

        hovered = False
    
        def __init__(self, text, pos):
            self.text = text
            self.pos = pos
            self.set_rect()
            self.draw()
            
        def draw(self):
            self.set_rend()
            screen.blit(self.rend, self.rect)
        
        def set_rend(self):
            self.rend = menu_font.render(self.text, True, self.get_color())
        
        def get_color(self):
            if self.hovered:
                return black
            else:
                return white
        
        def set_rect(self):
            self.set_rend()
            self.rect = self.rend.get_rect()
            self.rect.topleft = self.pos

    setting_txt = "SETTING = " + opsi_setting

    menu_font = pygame.font.Font(font, 40)
    text_start=text_format("START", font, 75, white)
    text_setting=text_format(setting_txt, font, 75, white)
    text_quit=text_format("QUIT", font, 75, white)

    start_rect=text_start.get_rect()
    setting_rect=text_setting.get_rect()
    quit_rect=text_quit.get_rect()

    options = [
        Option("START", (screen_width/2 - (start_rect[2]/4), 300)), 
        Option(setting_txt, (screen_width/2 - (setting_rect[2]/4), 360)),
        Option("QUIT", (screen_width/2 - (quit_rect[2]/4), 420))]
    
    pygame.display.update()
    pygame.display.set_caption("Connect 4")

    while True:
        pygame.event.pump()
        screen.fill(blue)
        for option in options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN and option.text == "START":
                        if opsi_setting == "ALPHA BETA":
                            os.system('connect4_alphabeta.py')
                        elif opsi_setting == "MINIMAX":
                            os.system('connect4_minimax.py')
                    if event.type == pygame.MOUSEBUTTONDOWN and option.text == setting_txt:
                        if opsi_setting == "ALPHA BETA":
                            opsi_setting = "MINIMAX"
                        elif opsi_setting == "MINIMAX":
                            opsi_setting = "ALPHA BETA"
                        mainmenu(opsi_setting)
                    if event.type == pygame.MOUSEBUTTONDOWN and option.text == "QUIT":
                        pygame.quit()
                        quit()
            else:
                option.hovered = False
        
            option.draw()
        title=text_format("CONNECT 4 AI", font, 90, yellow)
        title_rect=title.get_rect()
        
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        pygame.display.update()

    
        

mainmenu(opsi_setting)
pygame.quit()
QUIT()