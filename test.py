최선호
# 5428

최선호 — 2022.07
.15.
최선호
010 - 9227 - 0062
킴타요 — 2022.07
.15.
감사합니다
~
킴타요 — 오늘
오후
1: 06
1
import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'GWANGJU01_KIMTAEYOUNG'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    # 공의 지름
    r = 5.73
    HOLES = [[1, 1], [128, 1], [254, 1], [1, 126], [127, 126], [253, 126]]
    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    play1 = [3, 1, 5]  # 첫 턴이면 옆에 있는거 먼저 때리기
    play2 = [2, 4, 5]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    if order == 1:
...(147
줄
남음)
접기
GWANGJU01_KIMTAEYOUNG.py
11
KB
수정
중
﻿
import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'GWANGJU01_KIMTAEYOUNG'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    # 공의 지름
    r = 5.73
    HOLES = [[1, 1], [128, 1], [254, 1], [1, 126], [127, 126], [253, 126]]
    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    play1 = [3, 1, 5]  # 첫 턴이면 옆에 있는거 먼저 때리기
    play2 = [2, 4, 5]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    if order == 1:
        for b in play1:
            if balls[b][0] > 0:
                targetBall_x = balls[b][0]
                targetBall_y = balls[b][1]
                break

    elif order == 2:
        for b in play2:
            if balls[b][0] > 0:
                targetBall_x = balls[b][0]
                targetBall_y = balls[b][1]
                break

    # 임의 타격 위치
    shoot_x = targetBall_x
    shoot_y = targetBall_y

    # 홀 정하기
    for i in range(6):
        hole_x = HOLES[i][0]
        hole_y = HOLES[i][1]

        targetBall_hole_x = abs(targetBall_x - hole_x)
        targetBall_hole_y = abs(targetBall_y - hole_y)

        # 타격 위치 잡기

        target_x = targetBall_x
        target_y = targetBall_y

        if targetBall_x > hole_x and targetBall_y > hole_y:  # 치려고 하는 공(타겟공)이 홀 기준 1사분면에 있을 때
            targetBall_hole_radian = math.atan(targetBall_hole_x / targetBall_hole_y)  # 타겟 볼과 홀 사이의 라디안
            target_x += r * math.sin(targetBall_hole_radian)
            target_y += r * math.cos(targetBall_hole_radian)

        elif targetBall_x < hole_x and targetBall_y > hole_y:  # 2사분면에 있을 때
            targetBall_hole_radian = math.atan(targetBall_hole_x / targetBall_hole_y)
            target_x -= r * math.sin(targetBall_hole_radian)
            target_y += r * math.cos(targetBall_hole_radian)

        elif targetBall_x < hole_x and targetBall_y < hole_y:  # 3사분면에 있을 때
            targetBall_hole_radian = math.atan(targetBall_hole_x / targetBall_hole_y)
            target_x -= r * math.sin(targetBall_hole_radian)
            target_y -= r * math.cos(targetBall_hole_radian)

        elif targetBall_x > hole_x and targetBall_y < hole_y:  # 4사분면에 있을 때
            targetBall_hole_radian = math.atan(targetBall_hole_x / targetBall_hole_y)
            target_x += r * math.sin(targetBall_hole_radian)
            target_y -= r * math.cos(targetBall_hole_radian)

        # elif targetBall_x == hole_x:
        #     target_x -= r * math.cos(targetBall_hole_radian)
        # elif targetBall_y == hole_y:
        #     target_y -= r * math.cos(targetBall_hole_radian)

        # 타겟볼과 흰 공사이의 거리
        targetBall_whiteBall_distance = math.sqrt((targetBall_x - whiteBall_x) ** 2 + (targetBall_y - whiteBall_y) ** 2)

        # 타격 위치와 흰 공사이의 거리
        shoot_whiteBall_distance = math.sqrt((target_x - whiteBall_x) ** 2 + (target_y - whiteBall_y) ** 2)

        # 타겟 공과 가까운 홀 찾기
        targetBall_hole_distance_min = 10000

        # 타겟볼과 흰 공 사이의 거리가 타격 위치와 흰 공 사이의 거리보다 멀 때만 해당 홀로 공을 넣을 수 있음
        # 둔각 삼각형을 이룰 때

        if targetBall_whiteBall_distance > shoot_whiteBall_distance:
            targetBall_hole_distance = math.sqrt((targetBall_x - hole_x) ** 2 + (targetBall_y - hole_y) ** 2)
            if targetBall_hole_distance < targetBall_hole_distance_min:
                targetBall_hole_distance_min = targetBall_hole_distance
                shoot_x = target_x
                shoot_y = target_y

    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    if shoot_x > whiteBall_x and shoot_y > whiteBall_y:  # 실제 타격 위치가 흰 공기준 1사분면에 있을 때
        shoot_radian = math.atan(width / height)
        angle = 180 / math.pi * shoot_radian

    elif shoot_x < whiteBall_x and shoot_y > whiteBall_y:  # 2 사분면에 있을 때
        shoot_radian = math.atan(height / width)
        angle = (180 / math.pi * shoot_radian) + 270

    elif shoot_x < whiteBall_x and shoot_y < whiteBall_y:  # 3 사분면에 있을 때
        shoot_radian = float(math.atan(width / height))
        angle = (180 / math.pi * shoot_radian) + 180

    elif shoot_x > whiteBall_x and shoot_y < whiteBall_y:  # 4 사분면에 있을 때
        shoot_radian = float(math.atan(height / width))
        angle = (180 / math.pi * shoot_radian) + 90

    distance = math.sqrt(width ** 2 + height ** 2)
    power = distance
    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    # radian = math.atan(width / height) if height > 0 else 0
    # angle = 180 / math.pi * radian
    #
    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    # if whiteBall_x == targetBall_x:
    #     if whiteBall_y < targetBall_y:
    #         angle = 0
    #     else:
    #         angle = 180
    # elif whiteBall_y == targetBall_y:
    #     if whiteBall_x < targetBall_x:
    #         angle = 90
    #     else:
    #         angle = 270

    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    # if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
    #     radian = math.atan(width / height)
    #     angle = (180 / math.pi * radian) + 180

    # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    # elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
    #     radian = math.atan(height / width)
    #     angle = (180 / math.pi * radian) + 90
    #
    # # distance: 두 점(좌표) 사이의 거리를 계산
    # distance = math.sqrt(width**2 + height**2)
    # # power: 거리 distance에 따른 힘의 세기를 계산
    # power = distance * 0.5

    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    #
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')
GWANGJU01_KIMTAEYOUNG.py
11
KB