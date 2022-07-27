for test_case in range(1, int(input())+1):
    D, A, B, F = list(map(float, input().split(" ")))
    print(D, A, B, F)
    print('#{} {:.10f}'.format(test_case, D / (A + B) * F))