'''
99  9+9
18  8+1
09  9+0 99
99

'''
N = int(input())
before = N
now = -1
A, B = N // 10, N % 10
conut = 0
while conut < 5:
    print(now, A, B)
    conut += 1
    A, B = now // 10, now % 10

    if A:
        now = A + B

    else:
        now = before % 10 * 10 + B

    before = now

