for tc in range(1, 1 + int(input())):
    N, S = input().split()
    N = int(N)
    for i in S:
        print(i*N, end='')
    print()