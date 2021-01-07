#화면 크기 설정
import pygame

pygame.init() #초기화(필수)

#pygame을 이용해 간단한 게임 만들어 보기!

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/wallm/OneDrive/바탕 화면/PythonGame/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/wallm/OneDrive/바탕 화면/PythonGame/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해욤
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width/2) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치


#화면 타이틀 설정
pygame.display.set_caption("Nado game") #게임 이름

#이벤트 루프(프로그램이 종료하지 않도록 대기하는 것, 사용자의 입력을 체크함)
running = True  #게임이 진행중인지 확인
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가
            running = False

    # screen.fill((0,0,255)) fill 함수를 이용해서도 화면을 채울 수 있음
    screen.blit(background,(0,0)) #배경 그리기((0,0)은 x,y좌표를 가리킴)

    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update() # 게임 화면을 다시 그리기


#pygame 종료
pygame.quit()
