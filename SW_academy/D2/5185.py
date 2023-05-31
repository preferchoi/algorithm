def ten_to_two(N):
    ans = ''
    cnt = 0
    while cnt < 4:
        if N % 2:
            ans += '1'
        else:
            ans += '0'
        N //= 2
        cnt += 1
    return ans[::-1]


key = {}
for i in range(1 << 4):
    if i < 10:
        key[str(i)] = ten_to_two(i)
    else:
        key[chr(i+55)] = ten_to_two(i)

for tc in range(1, 1 + int(input())):
    N, s = input().split()
    print(f'#{tc}', end=' ')
    for i in s:
        print(key[i], end='')
    print()
