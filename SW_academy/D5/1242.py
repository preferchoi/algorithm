import sys

sys.stdin = open('../../text.txt', 'r')

dict_16 = {'0': '0000', '1': '0001',
           '2': '0010', '3': '0011',
           '4': '0100', '5': '0101',
           '6': '0110', '7': '0111',
           '8': '1000', '9': '1001',
           'A': '1010', 'B': '1011',
           'C': '1100', 'D': '1101',
           'E': '1110', 'F': '1111'}
dict_code = {211: 0,
             221: 1,
             122: 2,
             411: 3,
             132: 4,
             231: 5,
             114: 6,
             312: 7,
             213: 8,
             112: 9}

for tc in range(1, 1 + int(input())):
    y, x = map(int, input().split())
    lst = list(set([input().strip() for _ in range(y)]))
    lst.sort()
    lst = lst[1:]

    code_lst = set()
    for i in lst:
        code = ''
        for j in i:
            code += dict_16[j]
        code = code.rstrip('0')
        l1 = l2 = l3 = 0
        flag = True
        tmp = ''
        for j in range(len(code) - 1, -1, -1):
''
            if flag:
                if code[j] == '0' and l3:
                    flag = False
                    k = min(l1, l2, l3)
                    tmp += str(dict_code[l3 // k * 100 + l2 // k * 10 + l1 // k])
                    l1 = l2 = l3 = 0
                    if len(tmp) == 8:
                        code_lst.add(tmp[::-1])
                        tmp = ''
                elif code[j] == '1' and not l2:
                    l1 += 1
                elif code[j] == '0' and l1:
                    l2 += 1
                elif code[j] == '1' and l2:
                    l3 += 1

            else:
                if code[j] == '1':
                    flag = True
                    l1 += 1
                    continue
    ans = 0
    for i in code_lst:
        sumV = 0
        flag = True
        tmp = 0
        for j in i:
            if flag:
                sumV += int(j) * 3
                flag = False
            else:
                sumV += int(j)
                flag = True
            tmp += int(j)
        if not sumV % 10:
            ans += tmp

    print(f'#{tc} {ans}')

