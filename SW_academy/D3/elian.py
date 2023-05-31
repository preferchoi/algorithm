
num_rule = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
str_rule = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}
for test in range(1, int(input())+1):
    what = input().split(" ")
    array = input().split(" ")
    while '' in array:
        array.remove('')
    num_array = []
    for i in array:
        num_array.append(num_rule.get(i))

    num_array.sort()
    sort_array = []
    print(f'#{test}', end=" ")
    for i in num_array:
        print(str_rule.get(i), end=" ")
    print()
