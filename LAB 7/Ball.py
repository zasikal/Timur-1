import pygame
pygame.init()
 
Width = 500
Height = 300
x = 250
y = 150
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Ball")

N = True
while N:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            N = False



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y>50:
                y -= 20
            elif event.key == pygame.K_DOWN and y<250: 
                y += 20
            elif event.key == pygame.K_LEFT and x>50:
                x -= 20
            elif event.key == pygame.K_RIGHT and x<450:
                x += 20
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)

    pygame.display.flip()
pygame.quit()