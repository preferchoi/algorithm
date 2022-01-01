global sl
global lc

def stop(sn, en, sl, lc):
    w=list(range(sn, en+1))
    for i in range(len(sl)):
        if sl[i] in w:
            lc[i] += 1

for tc in range(1, 1+int(input())):
    N = int(input())
    bl = []
    for i in range(N):
        bl.append(list(map(int, input().split(" "))))
    P = int(input())
    sl = []
    for i in range(P):
        sl.append(int(input()))
    lc = [0]*P
    for i, j in bl:
        stop(i, j, sl, lc)

    # print(list_count)
    print(f'#{tc}', end=" ")
    for i in lc:
        print(i, end = " ")
    print()