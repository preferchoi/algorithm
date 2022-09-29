'''
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011

'''
def go(lst):
    cnt = 0
    key = lst[0][0]
    flag = False
    for y in lst:
        for x in y:
            if x != key:
                flag = True
                break
        if flag:
            break
    else:
        print(key)
        return key

    cut = len(lst)//2
    print(cut)
    tmp1, tmp2 = [], []
    for i in range(len(lst)):

    return lst

N = int(input())

lst_1 = [list(map(int, list(input()))) for _ in range(N)]
go(lst_1)