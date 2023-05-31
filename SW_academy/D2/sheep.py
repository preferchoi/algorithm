T = int(input())
# print(T)
for test_case in range(1, T + 1):
    N = int(input())
    x = N
    list = []
    y = 0
    # 숫자 몇자리인지 확인
    # print(len(str(N)))
    while True:
        for i in range(len(str(x))-1, -1, -1):
            # print(10**i)  1000, 100, 10, 1
            n = int(x/10**i) # 4321, 321, 21, 1
            # print('n', n)
            n2 = n*10**i # 4000, 300, 20, 1
            # print('n2', n2)
            x = x-n2 # 321, 21, 1, 0
            # print("x", x)
            # print(x)
            list.append(n)
        # print("추가 완료")
        # break
        # 각 자리수마다 있는 숫자 리스트에 추가
        # print(10**(len(str(N))-1))
        # 리스트 정렬, 중복제거 실행
        # print("리스트 정렬, 중복제거 실행")
        x = N * (y+1)

        list.sort()
        list2 = set(list)
        # print(list2)
        if list2 == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
            print("#{}".format(test_case), N*y)
            break
        y = y + 1

# 리스트에 0~9까지 있는지 확인
# 반복
# 반복 횟수 출력


