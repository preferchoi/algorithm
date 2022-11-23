T = int(input())
for test in range(1, T+1):
    string = '0'+input()
    count = 0
    print(f'#{test}', end=" ")
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            count += 1
    print(count)