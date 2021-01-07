# Project) 오락실 Pang 게임 만들기

# [게임조건]
# 1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
# 2. 스페이스바를 누르면 무기를 쏘아올림
# 3. 큰 공1개가 나타나면서 게임이 시작됨 
# 4. 무기에 닿으면 공기 2 등분 됨
# 5. 모든 공을 없애면 게임 종료
# 6. 캐릭터는 공에 닿으면 게임 종료
# 7. 시간제한 99초
# 8. fps는 30 으로

# [게임 이미지]
# 1. 배경 : 640 * 480 - background.png
# 2. 무대 : 640 * 50 - stage.png
# 3. 캐릭터 : 60 * 33 - character.png
# 4. 무기 : 20 * 430 -weapon.png
# 5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20 - ballon1.png ~ ballon4.png


import pygame
import os

##########################################################
#초기화(필수적으로 해야하는 것들)
pygame.init() 

#화면 크기 설정
screen_width = 640 #가로 크기
screen_height = 480 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Pang") #게임 이름

#화면 FPS
clock = pygame.time.Clock()

##########################################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트 등)
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path,"image") #images 폴더 위치 반환

background = pygame.image.load(os.path.join(image_path,"background.png"))

#stage 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이 위에 캐릭터를 두기 위해

character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size =  character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height - stage_height

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
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height - stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update() # 게임 화면을 다시 그리기

#pygame 종료
pygame.quit()
