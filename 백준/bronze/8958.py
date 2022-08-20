for tc in range(int(input())):
    s = input()
    cnt = 0
    ans = 0
    for i in s:
        if i == 'O':
            cnt += 1
        else:
            cnt = 0
        ans += cnt
    print(ans)