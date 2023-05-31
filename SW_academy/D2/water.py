T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = input()
    P, Q, R, S, W = string.split(" ")
    P, Q, R, S, W = int(P), int(Q), int(R), int(S), int(W)
    # print("P:", P, "Q:", Q, "R:", R, "S:", S, "W:", W)
    # a사
    payA = W * P
    # b사
    if R > W:
        payB = Q
    else:
        payB = (W-R)*S+Q
    # print("payA:", payA, "payB:", payB)
    if payA > payB:
        print("#{}".format(test_case), payB)
    else:
        print("#{}".format(test_case), payA)