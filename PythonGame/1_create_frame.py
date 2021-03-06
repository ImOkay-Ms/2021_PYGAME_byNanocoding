import pygame

pygame.init() #초기화(필수)

#pygame을 이용해 간단한 게임 만들어 보기!

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screem = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado game") #게임 이름

#이벤트 루프(프로그램이 종료하지 않도록 대기하는 것, 사용자의 입력을 체크함)
running = True  #게임이 진행중인지 확인
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가
            running = False

#pygame 종료
pygame.quit()
