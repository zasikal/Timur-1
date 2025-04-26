import pygame
import random
import psycopg2

pygame.init()

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydatabase",
    user="postgres",
    password="Stomap7406+" 
)
cur = conn.cursor()


def get_or_create_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
        cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
        score_level = cur.fetchone()
        if score_level:
            print(f"Добро пожаловать, {username}! Ваш текущий уровень: {score_level[1]}")
            return user_id, score_level[0], score_level[1]
        else:
            cur.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
            conn.commit()
            return user_id, 0, 0
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
        conn.commit()
        return user_id, 0, 0

def save_game(user_id, score, level):
    cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
    conn.commit()


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
food_pos = [0, 0]
special_food_pos = [0, 0]
food_spawn = False
special_food_spawn = False

walls = []

speed = 15
score = 0
level = 0
paused = False

def spawn_food():
    global food_pos, food_spawn, special_food_pos, special_food_spawn
    food_spawn = False
    special_food_spawn = False
    if random.randint(1, 5) == 1:
        special_food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        special_food_spawn = True
    else:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        food_spawn = True

def handle_events():
    global change_to, paused
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    save_game(user_id, score, level)
                    print("Игра на паузе и сохранена.")
            if not paused:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

def stena():
    if snake_pos[0] < 0:
        snake_pos[0] = WIDTH - 10
    elif snake_pos[0] >= WIDTH:
        snake_pos[0] = 0
    if snake_pos[1] < 0:
        snake_pos[1] = HEIGHT - 10
    elif snake_pos[1] >= HEIGHT:
        snake_pos[1] = 0

def move_snake():
    global direction, snake_pos, food_spawn, score, level, speed, special_food_spawn, food_pos, special_food_pos, walls

    direction = change_to
    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))

    if snake_pos == food_pos:
        score += 1
        if score >= level * 2 + 2:
            level_up()
        food_spawn = False
    elif snake_pos == special_food_pos:
        score += 5
        if score >= level * 2 + 2:
            level_up()
        special_food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn and not special_food_spawn:
        spawn_food()

def level_up():
    global level, speed, walls
    level += 1
    speed += 2
    walls = []
    if level >= 5:
        for i in range(50, 450, 40):
            walls.append([i, 200])
            walls.append([i, 300])

def draw():
    screen.fill(BLUE)
    font = pygame.font.Font(None, 30)
    score_txt = font.render(f"Score: {score}", True, WHITE)
    level_txt = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_txt, (10, 10))
    screen.blit(level_txt, (200, 10))

    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    if food_spawn:
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    if special_food_spawn:
        pygame.draw.rect(screen, GREEN, pygame.Rect(special_food_pos[0], special_food_pos[1], 10, 10))

    for wall in walls:
        pygame.draw.rect(screen, BLACK, pygame.Rect(wall[0], wall[1], 10, 10))

    pygame.display.flip()

def check_game_over():
    if snake_pos in snake_body[1:]:
        save_game(user_id, score, level)
        pygame.quit()
        quit()
    if snake_pos in walls:
        save_game(user_id, score, level)
        pygame.quit()
        quit()


username = input("Введите имя игрока: ")
user_id, score, level = get_or_create_user(username)
spawn_food()

if level >= 5:
    level_up()

while True:
    if not paused:
        stena()
        handle_events()
        move_snake()
        check_game_over()
        draw()
    else:
        handle_events()

    clock.tick(speed)
