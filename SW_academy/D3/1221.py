for tc in range(1, 1 + int(input())):
    N, P = input().split(" ")
    word_list = list(input().split())
    keys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    dict_1 = {key: 0 for key in keys}

    for i in word_list:
        dict_1[i] += 1
    print(N, end=' ')
    for i, j in dict_1.items():
        print(f'{i} ' * j, end='')
    print()