# KOREAKOREAKOREAKOREAKOREAKOREA
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = input()
    for i in range(1, 11):
        long = len(string[0:i])
        f_string = string[0:i]
        s_string = string[i:i+long]
        if f_string == s_string:
            # print("f_string:", f_string, "s_string:", s_string)
            print("#{}".format(test_case), long)
            break


# 이거 답 낼때 사용
# print(string.count("KOREA"))
