'''
8
4
3
6
8
7
5
2
1
'''
N = int(input())
N_list = [int(input()) for _ in range(N)]

now_num = 1
stack = []
ans = []
while now_num <= N:
    if not stack:
        stack.append(now_num)
        now_num += 1
        ans.append('+')
    else:
        if stack[-1] == N_list[0]:
            N_list.pop(0)
            stack.pop(-1)
            ans.append('-')
        else:
            stack.append(now_num)
            now_num += 1
            ans.append('+')
else:
    for i in stack[::-1]:
        if i == N_list.pop(0):
            stack.pop()
            ans.append('-')
if stack:
    print('NO')
else:
    for i in ans:
        print(i)
'''
+   [1]
+   [1, 2]
+   [1,2,3]
+   [1, 2, 3, 4]
-   [1, 2, 3] [4]
-   [1, 2] [4, 3] 
+   [1, 2, 5] [4,3]
+   [1,2,5,6][4,3]
-   [1,2,5][4,3,6]
+   [1,2,5,7][4,3,6]
+   [1,2,5,7,8][4,3,6]
-   [1,2,5,7][4,3,6,8]
-   [1,2,5][4,3,6,8,7]
-   [1,2][4,3,6,8,7,5]
-   [1][4,3,6,8,7,5,2]
-   [][4,3,6,8,7,5,2,1]
'''
