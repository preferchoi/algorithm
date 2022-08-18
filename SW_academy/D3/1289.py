for test in range(1, 1 + int(input())):
    s = '0'+input()
    cnt = 0
    print(f'#{test}', end=" ")
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            cnt += 1
    print(cnt)