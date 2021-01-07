import pygame

##########################################################
#초기화(필수적으로 해야하는 것들)
pygame.init() 

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado game") #게임 이름

#화면 FPS
clock = pygame.time.Clock()

##########################################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트 등)

#이벤트 루프(프로그램이 종료하지 않도록 대기하는 것, 사용자의 입력을 체크함)
running = True  #게임이 진행중인지 확인
while running:
    dt = clock.tick(30) 

    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가
            running = False

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기 

    pygame.display.update() # 게임 화면을 다시 그리기

#pygame 종료
pygame.quit()
