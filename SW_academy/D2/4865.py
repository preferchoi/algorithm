'''
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
'''

for tc in range(1, 1 + int(input())):
    key = list(input())
    lock = list(input())

    count = []
    for i in key:
        count.append(lock.count(i))

    print(f'#{tc} {max(count)}')