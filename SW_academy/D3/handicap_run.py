'''
5
5
10 70 30 50 90
2
30 100
2
100 20
3
40 40 40
7
12 345 678 901 23 45 6

'''
for test_case in range(1, int(input())+1):
    N = int(input())
    setting = list(map(int, input().split(" ")))
    max, min = 0, 0
    for i in range(1, len(setting)):
        if setting[i-1]-setting[i] > max:
            max = setting[i-1]-setting[i]
        if setting[i-1]-setting[i] < min:
            min = setting[i-1]-setting[i]

    print(f'#{test_case}', min*(-1), max)

