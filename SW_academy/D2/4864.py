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
    key = input()
    lock = input()

    N_key = len(key)
    ans = 0
    for i in range(len(lock) - N_key + 1):
        # print(lock[i:i+N_key])
        if lock[i:i+N_key] == key:
            ans = 1
            break
    print(f'#{tc} {ans}')