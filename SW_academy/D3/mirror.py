# for test in range(1, int(input())+1):
#     string = list(map(str, input()))
#     string.reverse()
#     print(f'#{test}', end=" ")
#     for i in string:
#         if i == 'q':
#             print('p',end="")
#         elif i == 'p':
#             print('q', end = "")
#         elif i == 'b':
#             print('d', end="")
#         elif i == 'd':
#             print('b', end="")
#     print()

for test in range(1, int(input())+1):
    A = list(map(str, input()))
    A.reverse()
    A0 = ''
    for i in A:
        A0 += i
    # print(f'#{test}', end=" ")
    A1_1 = A0.replace('q', '1')
    A1_2 = A1_1.replace('p', 'q')
    A1_3 = A1_2.replace('1', 'p')
    A2_1 = A1_3.replace('b', '2')
    A2_2 = A2_1.replace('d', 'b')
    A2_3 = A2_2.replace('2', 'd')
    print(f'#{test}', A2_3)