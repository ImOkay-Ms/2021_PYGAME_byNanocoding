#똥피하기 게임 만들기
import pygame
import random
##########################################################
#초기화(필수적으로 해야하는 것들)
pygame.init()

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Avoid Shit game") #게임 이름

#화면 FPS
clock = pygame.time.Clock()

##########################################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트 등)
#화면,이미지 data 가져오기
background = pygame.image.load("C:/Users/wallm/OneDrive/바탕 화면/PythonGame/background2.png")
character = pygame.image.load("C:/Users/wallm/OneDrive/바탕 화면/PythonGame/character2.png")
enemy = pygame.image.load("C:/Users/wallm/OneDrive/바탕 화면/PythonGame/enemy2.png")

#좌표설정
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width/2 - enemy_width/2
enemy_y_pos = 0

character_to_x = 0
character_to_y = 0
enemy_to_x = 0
enemy_to_y = 0

#타이머 설정
game_Font = pygame.font.Font(None,40)
start_ticks = pygame.time.get_ticks()

#이벤트 루프(프로그램이 종료하지 않도록 대기하는 것, 사용자의 입력을 체크함)
running = True  #게임이 진행중인지 확인

character_speed = 5
enemy_speed = 0.1

while running:
    dt = clock.tick(60) 
    # 3. 게임 캐릭터 위치 정의
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                    character_to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                    character_to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #여기서 event.key는
                character_to_x = 0

    character_x_pos += character_to_x
    character_y_pos += character_to_y

    #랜덤한 위치에서 생성되어 떨어지는 똥
    enemy_to_y += enemy_speed
    enemy_y_pos += enemy_to_y

    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randrange(1,480)  
        enemy_y_pos = 0
        enemy_to_y = 0

    #경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리
    #character 영역
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    #enemy 영역 설정 후 부딪히면 충돌함수 실행
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기 
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_Font.render(str(int(elapsed_time)),True,(255,255,0))
    screen.blit(timer,(10,10))
    pygame.display.update() # 게임 화면을 다시 그리기

#pygame 종료
pygame.quit()
