balls = [1,2,3,4]
weapons = [11,22,3,44]


# 우리가 발견한 문제점 break 이 2중 for 문에서 하나의 for문만 탈출함
# for ball_idx, ball in enumerate(balls):
#     print("ball : ", ball)
#     for weapon_idx, weapon in enumerate(weapons):
#         print("weapon : " , weapon)
#         if weapon == ball:
#             print("공과 무기가 충돌")
#             break 
        


# 해결책 for 문
for ball_idx, ball in enumerate(balls):
    print("ball : ", ball)
    for weapon_idx, weapon in enumerate(weapons):
        print("weapon : " , weapon)
        if weapon == ball:
            print("공과 무기가 충돌")
            break
    else:   #계속 게임을 진행
        print("else 문 실행 : ",weapon_idx  )
        continue    #안쪽 for문 조건이 맞지 않으면 continue, 바깥 for문 계속 수행

    print("바깥 for 문 break")
    break   #안쪽 for문에서 break를 만나면 여기로 진입 가능. 2중 for문을 한번에 탈출


    이 알고리즘은 암기해두는게 좋을듯!!