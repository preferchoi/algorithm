N_list = list(map(int, input().split()))
pre = N_list[0]
ans = ''
if pre == 1:
    ans = 'ascending'
    for i in N_list[1:]:
        if pre > i:
            ans = 'mixed'
            break
        pre = i
elif pre == 8:
    ans = 'descending'
    for i in N_list[1:]:
        if pre < i:
            ans = 'mixed'
            break
        pre = i
else:
    ans = 'mixed'
print(ans)