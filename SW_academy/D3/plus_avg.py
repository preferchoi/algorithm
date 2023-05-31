T = int(input())

for test in range(1, T+1):
    array = list(map(int, input().split(" ")))
    sum = 0
    for i in array:
        if i >= 40:
            sum += i
        else:
            sum += 40
    print(f'#{test}', int(sum/5))