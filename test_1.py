def wtf(lst, ans):
    if not sum(lst):
        print(ans)
        return
    for i in range(5):
        next_l = lst[:]
        next_a = ans[:]
        if next_l[i]:
            next_l[i] = 0
            next_a.append(i)
            wtf(next_l, next_a)


l = [True for _ in range(5)]
wtf(l, [])
