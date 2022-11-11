for tc in range(1, 11):
    N = int(input())
    N_list = list(map(int, input().split()))
    cnt = 0

    queue = []
    mid = N_list[2]

    for i in N_list:
        queue.append(i)
        # 대기열 q에 하나씩 집어넣었음
        # print(queue)
        if len(queue) > 5:
            queue.pop(0)
            mid = queue[2]
            # 6개 이상 넣었으면 맨 처음넣은거 하나 뺌

        # 5개 되면 돌아감
        if len(queue) == 5 and max(queue) == mid:
            # if문 들어올 때 중간이 최대값인거 확인
            max_2nd = 0
            # 두번째로 큰 값 찾는거
            for j in queue[:2] + queue[3:]:
                if max_2nd < j:
                    max_2nd = j
            # for j in queue:
            #     if max_2nd < j != mid:
            #         max_2nd = j
            # 이렇게 쓰면 안되는 이유 - 최대값이 여러개일 수 있기 때문에
            # 최대값이랑 같은게 두개면 빼도 결국 0이니까 ㄱㅊ
            cnt += mid - max_2nd
            # 최대값 - 두번째로 높은거 하면 조건 만족하는 칸만 뽑힘

    print(f'#{tc} {cnt}')