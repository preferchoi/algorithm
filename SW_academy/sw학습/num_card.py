'''
3
5
49679
5
08271
10
7797946543

'''

for test in range(int(input())):
    N = int(input())
    num_list = list(map(int, input()))
    dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for i in num_list:
        dict[str(i)] += 1

    max = 0
    max_key = 0
    for i in dict:
        if max <= dict[i]:
            max = dict[i]
            max_key = i
    print(f'#{test+1}',max_key, max)