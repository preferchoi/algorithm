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
    str1 = list(input())
    str1_idx = [0 for _ in range(len(str1))]
    str2 = input()

    for i in str2:
        for j in range(len(str1)):
            if i == str1[j]:
                str1_idx[j] += 1
    print(f'#{tc} {max(str1_idx)}')