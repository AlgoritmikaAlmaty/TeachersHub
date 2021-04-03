from pygame import *
from random import *
screen_width = 700
screen_height = 500
cl = time.Clock() #Подключаем работу со временем

score = 0 # сбито кораблей 

window = display.set_mode((screen_width, screen_height)) #создаю окно приложения с высотой и шириной
display.set_caption("Half Life 3") #Изменяем название окна

class Unit(sprite.Sprite): #Создаём класс
    def __init__(self, x, y, width, height, img):#Создаём конструкор класса
        #self.x = x не нужны
        #self.y = y не нужны
        self.width = width
        self.height = height
        self.image = image.load(img) #загружаем картинку в переменную image
        self.image = transform.scale(self.image, (width, height)) #изменяем размер image
        
        self.rect = self.image.get_rect() #получаю форму спрайта
        self.rect.x = x 
        self.rect.y = y

        # rect нужен для использования sprite.collide_rect(player, enemy)
        # sprite.collide_rect возвращает True или False
               
    def show(self): #Функция для отрисовки персонажа
        window.blit( self.image, (self.rect.x, self.rect.y) ) #Отображает на экран картинку

class Player(Unit):
    def move(self):
        keys = key.get_pressed()#получаем все нажатые клавиши
        if keys[K_LEFT]:
            self.rect.x -= 10
        if keys[K_RIGHT]:
            self.rect.x += 10
        if keys[K_UP]:
            self.rect.y -= 10
        if keys[K_DOWN]:
            self.rect.y += 10

player = Player(0,450,60,60, "cyborg.png") #Создаём объект класса            
            
run = True
while run:
    cl.tick(60)
    window.fill((255,255,255)) #Заливаю экран белым цвет

    for e in event.get(): #проверяем, нажали ли крестик
        if e.type == QUIT:
            run = False
            game_over_sound.play()
        
    player.move()
    player.show()

    


        #if sprite.collide_rect(i, enemies):
    
    
    
    display.update()


