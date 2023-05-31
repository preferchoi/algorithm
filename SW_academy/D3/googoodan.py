for test in range(1, int(input())+1):
    N = int(input())
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Ans = 'No'
    for i in num_list:
        count = 0
        if N // i < 10:
            count += 1

        if N % i == 0:
            count += 1

        if count == 2:
            Ans = 'Yes'
    print(f'#{test}', Ans)