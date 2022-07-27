# 맨 처음, 가격 리스트에서 최대값을 구한다.
# 그날 이전까지는 풀매수, 그날에 팔거니까 max 가격에 * len(list[:max] 한 다음 - sum(list[:max])
# 그 다음날부터 리스트 분할하고 다시 최대값 구하기
# 리스트 끝까지 오면 종료하고 총 이익 출력

'''
1
10
629 3497 7202 7775 4325 3982 4784 8417 2156 1932

1
50
5902 5728 8537 3857 739 6918 9211 9679 8506 3340 6568 1868 16 7940 6263 4593 1449 6991 310 3355 7068 1431 8580 1757 9218 4934 4328 3676 9355 6221 9080 5922 1545 8511 4067 5467 8674 4691 6504 9835 2034 4965 9980 1221 5895 2501 8152 8325 7731 9302

'''

T = int(input())

for test_case in range(1, T+1, 1):
    day = int(input())
    price = input().split(" ")

    for i in range(len(price)):
        price[i] = int(price[i])

    # print(price)

    Total = 0
    while len(price) != 0:
        sum = 0
        count = 0
        if len(price[:price.index((max(price)))]):
            price.remove(price[0])
            continue
        # print(price[:price.index(max(price))])
        for i in range(len(price[:price.index(max(price))])):
            sum += price[0]
            count += 1
            price.remove(price[0])
        # print(sum, count)
        Total += price[0] * count - sum
        price.remove(price[0])
        # print(price)
    print(f'#{test_case}', str(Total))
