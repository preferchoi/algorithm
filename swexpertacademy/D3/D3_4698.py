a_list = [True for _ in range(1000001)]
a_list[0], a_list[1] = False, False

for i in range(1000001):
    if a_list[i]:
        for j in range(i*2, 1000001, i):
            a_list[j] = False

for tc in range(1, 1 + int(input())):
    D, start, end = map(int, input().split())

    cnt = 0
    for i in range(start, end + 1):
        tmp = i
        if a_list[tmp]:
            while tmp:
                if tmp % 10 == D:
                    cnt += 1
                    break
                tmp //= 10
    print(f'#{tc} {cnt}')
