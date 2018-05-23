import pygame

pygame.init()
#Параметры экрана
display_w = 900
display_h = 900


gameDisplay = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

done = False

while not done:
    # Обработчик событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True

        #print(e)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()