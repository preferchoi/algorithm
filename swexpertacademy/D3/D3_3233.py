for test_case in range(1, int(input())+1):
    AB = list(map(int, input().split(' ')))
    A, B = AB[0], AB[1]
    slash = A//B
    sum = 0
    for i in range(slash, 0, -1):
        sum += i
    ans = 2*sum-slash
    print(f'#{test_case}', ans)