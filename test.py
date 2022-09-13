def inorder(now):
    global cnt
    if now == 0:
        return
    cnt += 1
    inorder(left[now])
    inorder(right[now])


T = int(input())
for testcase in range(1, T + 1):
    E, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(arr)
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    for i in range(0, len(arr), 2):
        parents, child = arr[i], arr[i + 1]
        # print(parents, child)
        # 부모 인덱스가 비었을때 왼쪽 자식값에 먼저 저장
        if left[parents] == 0:
            left[parents] = child
        # 이미 채워져 있을때 오른쪽 자식값에 저장
        else:
            right[parents] = child
    # print(left)
    # print(right)
    cnt = 0
    inorder(M)
    print(f'#{testcase} {cnt}')

