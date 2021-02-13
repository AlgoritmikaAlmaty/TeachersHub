from pygame import *
screen_width = 700
screen_height = 500

window = display.set_mode((screen_width, screen_height)) #создаю окно приложения с высотой и шириной
display.set_caption("Half Life 3") #Изменяем название окна

class Unit(): #Создаём класс
    def __init__(self, x, y, width, height, img):#Создаём конструкор класса
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.image = image.load(img) #загружаем картинку в переменную image
        self.image = transform.scale(self.image, (width, height)) #изменяем размер image
        
        
    def show(self): #Функция для отрисовки персонажа
        window.blit( self.image, (self.x, self.y) ) #Отображает на экран картинку


class Player(Unit):
    def move(self):
        keys = key.get_pressed()#получаем все нажатые клавиши
        if keys[K_LEFT]:
            self.x -= 10
        if keys[K_RIGHT]:
            self.x += 10
        if keys[K_UP]:
            self.y -= 10
        if keys[K_DOWN]:
            self.y += 10

run = True
while run:
    time.delay(50)

    window.fill((255,255,255)) #Заливаю экран белым цветом

    for e in event.get(): #проверяем, нажали ли крестик
        if e.type == QUIT:
            run = False

    player.move()
    player.show()
    enemy.show()
    
    display.update()
