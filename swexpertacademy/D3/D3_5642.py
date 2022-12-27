T = int(input())

for t in range(1, T+1) :
    N = int(input())
    number = list(map(int, input().split()))

    sum = number[0]
    for i in range(N-1) :
        if number[i] >= 0 and (number[i] + number[i+1] >= 0) :
            number[i+1] += number[i]
        if sum < number[i+1] :
            sum = number[i+1]

    print("#{} {}".format(t, sum))