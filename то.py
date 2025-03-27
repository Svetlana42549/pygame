import pygame

class Food:
    def __init__(self, u, m, t):
        self.image = pygame.image.load(u)
        self.rect = self.image.get_rect()
        self.x = m
        self.y = t
    def rendering_method(self):
        screen.blit(self.image, ())

fon = Food('кухня.jpg', 0, 0)
pygame.init() #обязательная команда
window_size=(1000, 1000) #размеры окна
screen=pygame.display.set_mode(window_size) #создаем экран
pygame.display.set_caption("")
background_color = (0, 0, 255) #создание цвета
clock = pygame.time.Clock() #создание игрщвого таймера
font =  pygame.font.SysFont("arial", 10) #создание  шрифта
text = font.render('человек', True,(255,255,255)) #создание текста на основе шрифта
y = 150
x = 150



while True: #игровой цикл
    screen.blit(self.image, (0, 0))#создание картинки
    r = pygame.Rect(x, y, 100, 50)  # создание прямоугольника
    clock.tick(40) #чистота обновление сцены

    pygame.draw.rect(screen,(0,0,0),r) #отрисовка прямоугольника
    screen.blit(text, (150, 150)) #тображение текста
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y = y - 5
            if event.key == pygame.K_d:
                x = x + 5
            if event.key == pygame.K_s:
                y = y + 5
            if event.key == pygame.K_a:
                x = x - 5


    if event.type == pygame.QUIT:  # если нажали на крестик
        pygame.QUIT()  # выход из игры
    pygame.display.update()  # обновление содержимого экрана

