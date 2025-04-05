import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)
BLUE = (50, 153, 213)



snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction
food_pos = [0, 0]   #чтоб не было проблем потом
special_food_pos = [0, 0]
food_spawn = False
special_food_spawn = False

#функция рандомно спавнит обычный или спешл фрукт
def spawn_food():
    global food_pos, food_spawn, special_food_pos, special_food_spawn
    food_spawn = False
    special_food_spawn = False
    if random.randint(1, 5) == 1:  #1/5 
        special_food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        special_food_spawn = True

    else:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        food_spawn = True

speed = 15
score = 0
lvl = 0

def handle_events():
    global change_to
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
#чтоб не вылетало когда врезаешься в стенку
def stena():
    if snake_pos[0] < 0:  #если выходит за левую границу
        snake_pos[0] = WIDTH - 10
    elif snake_pos[0] >= WIDTH:  #если выходит за правую границу
        snake_pos[0] = 0
    if snake_pos[1] < 0:  #если выходит за верхнюю границу
        snake_pos[1] = HEIGHT - 10
    elif snake_pos[1] >= HEIGHT:  #если выходит за нижнюю границу
        snake_pos[1] = 0   

def move_snake():
    global direction, snake_pos, food_spawn, score, lvl, speed, special_food_spawn, food_pos, special_food_pos
    direction = change_to
    if change_to == 'UP':
        snake_pos[1] -= 10
    elif change_to == 'DOWN':
        snake_pos[1] += 10
    elif change_to == 'LEFT':
        snake_pos[0] -= 10
    elif change_to == 'RIGHT':
        snake_pos[0] += 10
    
    
    snake_body.insert(0, list(snake_pos))

    if snake_pos == food_pos: #учет лвла
        score += 1
        if score == lvl*2 + 2:
            lvl += 1
            speed += 1
        food_spawn = False
        special_food_spawn = False
    elif snake_pos == special_food_pos:
        score += 5
        if score == lvl*2 + 2:
            lvl += 1
            speed += 1
        special_food_spawn = False
        food_spawn = False
        spawn_food()

    else:
        snake_body.pop()

    
    if not food_spawn and not special_food_spawn:
        spawn_food()

def draw():
    screen.fill(BLUE)
    score_txt = pygame.font.Font(None, 30).render(f"Score: {score}", True, WHITE)
    screen.blit(score_txt, (10, 10))
    lvl_txt = pygame.font.Font(None, 30).render(f"Lvl: {lvl}", True, WHITE) #иконка лвла
    screen.blit(lvl_txt, (200, 10))
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    if food_spawn:
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    if special_food_spawn: #рисуем спец фрукт
        pygame.draw.rect(screen, GREEN, pygame.Rect(special_food_pos[0], special_food_pos[1], 10, 10))
    pygame.display.flip()


def check_game_over():
    for block in snake_body[1:]:
        if snake_pos == block:
            pygame.quit()
            quit()
spawn_food()




while True:

    stena()
    handle_events()
    move_snake()
    check_game_over()
    draw()
    clock.tick(speed)
