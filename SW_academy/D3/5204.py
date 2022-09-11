'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

'''
def slice(lst):
    global cnt
    left, right = lst[:len(lst)//2], lst[len(lst)//2:]
    if len(left) > 1:
        left = slice(left)
    if len(right) > 1:
        right = slice(right)

    if left[-1] > right[-1]:
        cnt += 1
    ans = left + right
    ans.sort()
    return ans

for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = list(map(int, input().split()))
    cnt = 0
    a = slice(N_list)
    print(f'#{tc}', a[N//2], cnt)