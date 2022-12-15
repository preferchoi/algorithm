for tc in range(1, 1 + int(input())):
    s = list(input())
    q = True
    for i in range(0, len(s)):
        s[i], s[-(i+1)]
        if s[i] == '?' or s[-(i+1)] == '?' or s[i] == s[-(i+1)]:
            continue
        else:
            q = False
            break
    if q:
        print(f'#{tc} Exist')
    else:
        print(f'#{tc} Not exist')