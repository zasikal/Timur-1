#Imports
import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
C = 0  #Нач колво монет


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
#надпись нажмите р чтоб возрадиться
Dead = pygame.font.Font(None, 30).render("To restart press R", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#Инициализация класса коин (тоже самое почти что и энэми)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rposition()
    
    def rposition(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
#тоже самое
class SuperCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin2.jpg")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rposition()
    
    def rposition(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


#функция на рандом какой коин заспавнит
def spawn_coin():
    if random.randint(1, 5) == 1:
        return SuperCoin()
    else:
        return Coin()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)




P1 = Player()
E1 = Enemy()
C1 = spawn_coin()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


def restart():
    global SCORE, SPEED, C, C1
    C = 0
    SCORE = 0
    SPEED = 5
    # Reset player and enemy positions
    P1.rect.center = (160, 520)
    E1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    C1 = spawn_coin()
    enemies.empty()
    enemies.add(E1)
    coins.empty()
    coins.add(C1)
    all_sprites.empty()
    all_sprites.add(P1)
    all_sprites.add(E1)
    all_sprites.add(C1)



while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    #справа сверху колво коинов
    Cns = font_small.render(str(C), True, (255,175,10))
    DISPLAYSURF.blit(Cns, (380, 10))

 


    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()





    
    if pygame.sprite.spritecollideany(P1, coins): #есть ли пробитие коина
        for coin in coins:
            if isinstance(coin, SuperCoin): #если является суперкоином в картеже коин
                C += 3
            else:
                C += 1
        if C%5==1: #увеличиваем скорость за каждые 5 монет
            SPEED += C/10
        coins.empty() #очищаем от спрайтов
        all_sprites.remove(C1) #удаляет монету предыдущую
   
        C1 = spawn_coin() #новый спрайт
        coins.add(C1)
        all_sprites.add(C1)





    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)                   
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(Dead, (100, 450)) 
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        
        #кнопка для возраждения
        Die= True
        while Die:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart() 
                        Die = False   

    pygame.display.update()
    FramePerSec.tick(FPS)
