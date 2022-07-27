# 월은 1 이상 12 이하의 정수이다. 각 달의 마지막 날짜는 다음과 같다.
# 1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
# 두 번째 날짜가 첫 번째 날짜보다 항상 크게 주어진다.
# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 4개의 수가 주어진다.
# 첫 번째 수가 월을 나타내고 두 번째 수가 일을 나타낸다. 그 다음 같은 형식으로 두 번째 날짜가 주어진다.

m_d_dir = {"1": 31, "2": 28, "3": 31, "4": 30, "5": 31, "6": 30,
           "7": 31, "8": 31, "9": 30, "10": 31, "11": 30, "12": 31}
T = int(input())
for test_case in range(1, T + 1):
    A = 0
    inp = input()
    # print(inp.split(" "))
    f_month, f_day, s_month, s_day = inp.split(" ")
    f_month = int(f_month)
    f_day = int(f_day)
    s_month = int(s_month)
    s_day = int(s_day)

    # 월이 같으면 s_day 에서 f_day 를 뺀 다음 +1
    if f_month == s_month:
        A = s_day - f_day + 1

    # 월이 다르면??
    if f_month != s_month:
        for i in range(f_month, s_month + 1, 1):
            if i == f_month:
                # print("처음", i, "월")
                A += m_d_dir[str(i)] - f_day + 1
            elif i == s_month:
                # print("끝", i, "월")
                A += s_day
            else:
                # print(i, "월", m_d_dir[str(i)])
                A += m_d_dir[str(i)]
    print("#{}".format(test_case), A)