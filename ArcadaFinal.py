from pygame import *
from random import *
screen_width = 700
screen_height = 500
cl = time.Clock() #Создаём таймер

shift = 0

background = transform.scale(image.load("background.png"),(screen_width,screen_height)) #Создаём бэкграунд и меняем ему размер

window = display.set_mode((screen_width, screen_height)) #создаю окно приложения с высотой и шириной
display.set_caption("Half Life 5") #Изменяем название окна

class Unit(sprite.Sprite): #Создаём класс
    def __init__(self, x, y, width, height, img):#Создаём конструкор класса
        sprite.Sprite.__init__(self)
        self.x = x #Начальные координата х
        self.y = y #Начальная координата у
        self.width = width #Сохраняем ширину
        self.height = height #Сохраняем высоту
        self.image = image.load(img) #загружаем картинку в переменную image
        self.image = transform.scale(self.image, (width, height)) #изменяем размер image
        
        self.rect = self.image.get_rect() #получаю форму спрайта
        self.rect.x = x 
        self.rect.y = y

        # rect нужен для использования sprite.collide_rect(player, enemy)
        # sprite.collide_rect возвращает True или False
        self.y_speed = 0
               
    def show(self): #Функция для отрисовки персонажа
        window.blit( self.image, (self.rect.x, self.rect.y) ) #Отображает на экран картинку

class Player(Unit):
    def move(self):
        global shift
        keys = key.get_pressed()#получаем все нажатые клавиши
        if keys[K_LEFT]:
            #self.rect.x -= 3
            shift += 3
        if keys[K_RIGHT]:
            #self.rect.x += 3
            shift -= 3
        if keys[K_UP]:
            self.rect.y -= 5
        if keys[K_DOWN]:
            self.rect.y += 5
        
        if not sprite.spritecollide(self, walls, False): #Проверяем коллизию
            self.y_speed += 0.2
        else:
            self.y_speed = 0
            if keys[K_SPACE]:
                self.y_speed = -3



    def show(self): #Функция для отрисовки персонажа
        
        self.rect.y = self.rect.y + self.y_speed 
        window.blit( self.image, (self.rect.x, self.rect.y) ) #Отображает на экран картинку
    
    def jump(self): #Функция для отрисовки персонажа
        self.y_speed = -5
        self.rect.y = self.rect.y + self.y_speed

class Enemy(Unit):
    pointLeft = 0 #Правая граница для патрулирования
    pointRight = 0 #Левая граница для патрулирования
    speed = 3 #Скорость персонажа
    isLeft = False #Направление движения

    def move(self):
        a = randint(1, 4)
        if a == 1:
            self.y -= 2
        if a == 2:
            self.y += 2
        if a == 3:
            self.x -= 2
        if a == 4:
            self.x += 2

    def patrol(self): 
        if self.isLeft: #Если направление - влево, то
            self.x -= self.speed # Идем влево
        else: #В противном случае
            self.x += self.speed #Идем вправо
        if self.x < self.pointLeft: #Если персонаж перешел левую границу, то
            self.isLeft = False #Меняем направление вправо
        if self.x > self.pointRight: #Если персонаж перешел правую границу, то
            self.isLeft = True #Меняем направление влево

    def show(self):
        global shift
        self.rect.x = self.x
        self.rect.x += shift
        self.rect.y = self.y
        window.blit( self.image, (self.rect.x, self.rect.y) ) #Отображает на экран картинку

class Wall(sprite.Sprite):
    def __init__(self, x=20, y=0, width=120, height=120, color=(255,255,255)):
        sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        # картинка - новый прямоугольник нужных размеров:
        self.image = Surface([width, height])
        self.image.fill(color)
        # создаем свойство rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def show(self):
        global shift 
        self.rect.x = self.x
        self.rect.x += shift

        window.blit( self.image, (self.rect.x , self.rect.y)  )



player = Player(screen_width/2,screen_height/2,70,70,'1-2.png')
enemy = Enemy(screen_width/2 + 200,400 - 120,80,80, "2-2.png")
enemy2 = Enemy(50,50,80,80, "2-2.png")
enemy2.pointLeft = 0
enemy2.pointRight = 500

wall1 = Wall(300,400,150,50)
wall2 = Wall(400,350,150,50)

walls = sprite.Group()
walls.add(wall1)
walls.add(wall2)

enemy1 = Enemy(600,400,80,80, "2-2.png")

enemies = sprite.Group()
enemies.add(enemy)
enemies.add(enemy1)
enemies.add(enemy2)


a = 0
run = True
while run:
    
    cl.tick(60) #time.delay(60)
    window.blit(background, (shift,0))
    window.blit(background, (shift - screen_width,0))
    window.blit(background, (shift + screen_width,0))

    wall1.show()
    
    for e in event.get(): #проверяем, нажали ли крестик
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_w:
                print(1)
                player.jump()
                
    if sprite.collide_rect(player, wall1):
        print(a)
        a += 1
    for i in walls: #Проходимся по каждой стене в списке
        i.show() #Отображаем её

    player.move()
    player.show()
    
    for i in enemies:
        i.show()
        
    enemy1.move()
    enemy.move()    
    enemy2.patrol()
    
    
    #spritecollide

    display.update()
