'''
2
1 2
100000000000000000000000001 9

'''

for tc in range(1, 1+ int(input())):
    AB = input().split()
    A, B = list(AB[0]), list(AB[1])
    A.reverse()
    B.reverse()
    ans = []
    mini_str = ''
    set_num = 0
    if len(A) > len(B):
        set_num = len(B)
        for i in range(len(B)):
            ans.append(int(A[i])+int(B[i]))
        for i in range(set_num, len(A)):
            ans.append(A[i])
    else:
        set_num = len(A)
        for i in range(len(A)):
            ans.append((int(A[i])+int(B[i])))
        for i in range(set_num, len(B)):
            ans.append(B[i])
    for i in range(1, len(ans)):
        ans[i] = int(ans[i])
        if ans[i-1] >= 10:
            ans[i] += 1
            ans[i-1] -= 10
    ans.reverse()
    for i in ans:
        mini_str += str(i)
    print(mini_str)