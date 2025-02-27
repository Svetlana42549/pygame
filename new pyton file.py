import pygame
pygame.init() #обязательная команда
window_size=(300, 300) #размеры окна
screen=pygame.display.set_mode(window_size) #создаем экран
pygame.display.set_caption("")
background_color = (0, 0, 255) #создание цвета
screen.fill(background_color) #зфливаем экран цветом
clock = pygame.time.Clock() #создание игрщвого таймера
r = pygame.Rect(150, 150, 100, 50 ) #создание прямоугольника
font =  pygame.font.SysFont("arial", 10) #создание  шрифта
text = font.render('человек', True,(255,255,255)) #создание текста на основе шрифта
while True: #игровой цикл
    clock.tick(40) #чистота обновление сцены
    pygame.display.update() #обновление содержимого экрана
    pygame.draw.rect(screen,(0,0,0),r) #отрисовка прямоугольника
    screen.blit(text, (150, 150)) #тображение текста
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            pygame.QUIT()  # выход из игры

