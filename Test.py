import pygame #Подключаем модуль
from random import *
pygame.init() #Активируем

#Создаём окно и перекрашиваем
window = pygame.display.set_mode( (500,500) )


clock = pygame.time.Clock() #Создали таймер

COLOR_PURPLE = (255,0,255)

font = pygame.font.SysFont('verdana', 30) #Создаём шрифт


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height) 
        self.fill_color = color
        self.text = font.render("", True, (0,0,0))
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
        window.blit(self.text, (self.rect.x,self.rect.y + 25))
    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness) 
    def set_text(self,text1):
        self.text=font.render(text1,True,(0,0,0))



kvadrad1= Area(50,50,50,70,COLOR_PURPLE)
kvadrad2= Area(150,50,50,70,COLOR_PURPLE)
kvadrad3= Area(250,50,50,70,COLOR_PURPLE)
kvadrad4= Area(350,50,50,70,COLOR_PURPLE)

cards = [ kvadrad1, kvadrad2, kvadrad3, kvadrad4 ]

def random_cards():
    a=randint(0,3)
    for i in range(4):
        if i ==a:
            cards[i].set_text("click")
        else:
            cards[i].set_text("")

pygame.display.update()

run = True
timer = 0

while run:
    clock.tick(40)
    timer += 1
    if timer >= 40:
        random_cards()
        timer = 0 

    window.fill( (255,255,0) )
    
    for i in cards:
        i.fill()

    pygame.display.update()
