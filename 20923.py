'''
10 12
1 2
2 2
1 2
2 3
3 1
2 2
2 5
2 1
5 1
2 3

'''
from collections import deque

N, M = map(int, input().split())

su_list, do_list = deque([]), deque([])

for i in range(N):
    Su_num, Do_num = map(int, input().split())
    su_list.appendleft(Su_num)
    do_list.appendleft(Do_num)

start = True
su_ground, do_ground = deque(), deque()

for i in range(M):
    # print(i, su_list, do_list)
    if start:
        su_ground.appendleft(su_list.pop())

        start = False
    else:
        do_ground.appendleft(do_list.pop())

        start = True

    if su_ground and do_ground:
        if len(su_ground) == 1 and len(do_ground) == 1:
            if start:
                if start:
                    pass

                elif su_ground[0] + do_ground[0] == 5:
                    do_ground.reverse()
                    do_list.extendleft(do_ground)
                    su_ground.reverse()
                    do_list.extendleft(su_ground)
                    su_ground, do_ground = deque(), deque()
        elif su_ground == 5 or do_ground[0] == 5:
            su_ground.reverse()
            do_list.extendleft(su_ground)
            do_ground.reverse()
            do_list.extendleft(do_ground)
            su_ground, do_ground = deque(), deque()
        elif su_ground[0] + do_ground[0] == 5:
            do_ground.reverse()
            do_list.extendleft(do_ground)
            su_ground.reverse()
            do_list.extendleft(su_ground)
            su_ground, do_ground = deque(), deque()
    # print(su_list, do_list)
    if not su_list:
        break
    if not do_ground:
        break

if len(su_list) > len(do_list):
    print('su')
elif len(su_list) < len(do_list):
    print('do')
else:
    print('dosu')
