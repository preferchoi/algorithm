for tc in range(1, 1+ int(input())):
    mapp = list(input())
    # print(mapp)
    # while '|' in mapp:
    #     mapp.remove('|')


    count = 0
    ans = 0
    before = ''
    for i in mapp:
        if i in [')', '|'] and before == '(':
            ans += 1
        elif before in ['(', '|'] and i == ')':
            ans += 1
        before = i
    print(f'#{tc} {ans}')