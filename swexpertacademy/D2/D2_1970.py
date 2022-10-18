T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    f_m = N//50000
    N = N % 50000
    m = N // 10000
    N = N % 10000
    f_t = N // 5000
    N = N % 5000
    t = N // 1000
    N = N % 1000
    f_h = N // 500
    N = N % 500
    h = N // 100
    N = N % 100
    f_st = N // 50
    N = N % 50
    st = N // 10
    N = N % 10

    print(f'#{test_case}')
    print(f_m, m, f_t, t, f_h, h, f_st, st)