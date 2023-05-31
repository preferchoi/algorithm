T = int(input())

for test in range(1, T+1):
    rng = list(map(int, input().split(" ")))
    count_A = 0
    for i in range(rng[0], rng[1]+1):
        count = 0
        A = 0
        # print(f'#{i}', i, i**0.5)
        for j in range(len(str(i))):
            if str(i)[j] == str(i)[len(str(i))-j-1]:
                count += 1
                if count == len(str(i)):
                    # print(i)
                    A += 1
        count = 0
        if i**0.5 - int(i**0.5) == 0:
            pow_i = int(i**0.5)
            # print(i)

            for j in range(len(str(pow_i))):
                if str(pow_i)[j] == str(pow_i)[len(str(pow_i)) - j - 1]:
                    count += 1
                    if count == len(str(pow_i)):
                        # print(pow_i)
                        A += 1

        if A == 2:
            count_A += 1
    print(f'#{test}', count_A)