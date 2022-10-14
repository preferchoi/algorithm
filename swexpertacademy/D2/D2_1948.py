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