import pygame

pygame.init()
pygame.mixer.init()
#создаем экран
Width = 500
Height = 250
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Music Player") #название
#шрифт
font = pygame.font.Font(None, 40)

#не мой плейлист
playlist = [
    'two.mp3',
    'Быть счастливой.mp3',
    'Все на своих местах.mp3',
    'Красавица.mp3',
    'Не люби меня.mp3',
    'Помнишь.mp3'
]
playing = False
song = 0
pygame.mixer.music.load(playlist[song]) #аплоудим плейлист в миксер для работы с музокой
#включить музыку
def play_music():
    global playing
    pygame.mixer.music.play()
    playing = True
#выключить музыку
def stop_music():
    global playing
    pygame.mixer.music.stop()
    playing = False
#след музыка
def next_music():
    global song, playing
    song = (song + 1) % len(playlist)
    pygame.mixer.music.load(playlist[song])
    if playing == True:
        pygame.mixer.music.play()  
#пред музыка
def prev_music(): 
    global song, playing
    song = (song - 1) % len(playlist)
    pygame.mixer.music.load(playlist[song])
    if playing == True:
        pygame.mixer.music.play()


font2 = pygame.font.Font(None,20) #еще 1 шрифт
def info(): #информация о музыке и кнопочки
    global ts1, ts2, ts3, ts4
    name = playlist[song]
    number = song +1 
    text = f"song {number}: {name}"
    screen.blit(pygame.font.Font(None, 20).render(text, True, (255, 255, 255)), (0, 0))
    t1 = "Play the song"
    screen.blit(font2.render(t1, True, (255, 255, 255)), (0, 30))
    ts1 = font2.render(t1, True, (255, 255, 255)).get_rect(topleft =(0, 30))
    t2 = "Stop the song"
    screen.blit(font2.render(t2, True, (255, 255, 255)), (300, 30))
    ts2 = font2.render(t1, True, (255, 255, 255)).get_rect(topleft =(300, 30))
    t3 = "Next song"
    screen.blit(font2.render(t3, True, (255, 255, 255)), (0, 90))
    ts3 = font2.render(t1, True, (255, 255, 255)).get_rect(topleft =(0, 90))
    t4 = "Previous song"
    screen.blit(font2.render(t4, True, (255, 255, 255)), (300, 90))
    ts4 = font2.render(t1, True, (255, 255, 255)).get_rect(topleft =(300, 90))  




N = True
while N: 
    screen.fill((0, 0, 0))
    info()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            N = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 150 <= mouse_pos[0] <= 150 + 200 and 200 <= mouse_pos[1] <= 200 + 60: #при нажатии на кнопку выход выйти
                if event.button == 1:
                    N = False 
        if event.type == pygame.MOUSEBUTTONDOWN: #при нажатии на кнопки выход
            mouse_pos = pygame.mouse.get_pos()
            if ts1.collidepoint(mouse_pos):
                play_music()
            if ts2.collidepoint(mouse_pos):
                stop_music()
            if ts3.collidepoint(mouse_pos):
                next_music()
            if ts4.collidepoint(mouse_pos):
                prev_music()

        if event.type == pygame.KEYDOWN: #стрелками переключать
            if event.key == pygame.K_UP:
                if not playing:
                    play_music()
            elif event.key == pygame.K_DOWN: 
                stop_music()
            elif event.key == pygame.K_LEFT:
                prev_music()
            elif event.key == pygame.K_RIGHT:
                next_music()

    pygame.draw.rect(screen, (0, 0, 255), (150, 200, 200, 60))  #сама кнопка выйти
    label = font.render("Выйти", True, (255, 0, 0))  
    screen.blit(label, (150 + (200 - label.get_width()) // 2, 200 + (60 - label.get_height()) // 2))  
    

  
    pygame.display.flip()




pygame.quit()