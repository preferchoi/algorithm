'''
4
4 9 1
4 9 2
4 9 3
500 2000 2000000000

'''


def change(x, y, k):
    pass


for tc in range(1, 1 + int(input())):
    A, B, K = map(int, input().split())
    if A < B:
        X, Y = B, A
    else:
        X, Y = A, B

    change(A, B, K)
