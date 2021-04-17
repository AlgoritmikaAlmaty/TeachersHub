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
