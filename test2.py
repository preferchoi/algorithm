T = int(input())
for testcase in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    lst = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            lst.append(arr[i] * arr[j])

    MAX = -21e8
    for num in lst:
        word = str(num)
        for m in range(len(word) - 1):
            if word[m] < word[m + 1]:
                if MAX < num:
                    MAX = num

    print(f'#{testcase} {MAX}')
