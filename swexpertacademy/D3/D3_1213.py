for test in range(1, 11):
    N = input()
    key = list(map(str, input()))
    string = list(map(str, input()))
    A = 0
    for i in range(len(string)-len(key)+1):
        count = 0
        for j in range(len(key)):
            if key[j] == string[i+j]:
                count += 1
        if count == len(key):
            A += 1
    print(f'#{test}', A)