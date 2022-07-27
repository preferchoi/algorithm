'''
2
3
1 3 2
5
1 3 5 4 2
'''
for t in range(int(input())):
    N, s, c = int(input()), list(map(int, input().split(" "))), 0
    for i in range(1, N-1):
        if s[i-1] < s[i] < s[i+1] or s[i+1] < s[i] < s[i-1]:
            c += 1
    print(f'#{t+1}', c)