'''
두 개의 전구 X와 Y가 있다. 당신은 0초에서부터 시작하여 100초간 두 전구가 언제 켜지는지를 관찰하였다.
관찰 결과, 전구 X는 관찰 시작 경과 후 A초에서부터 관찰 시작 경과 후 B초까지에만 켜져 있었다.
전구 Y는 관찰 시작 경과 후 C초에서부터 관찰 시작 경과 후 D초까지에만 켜져 있었다.
당신이 두 전구를 관찰하던 100초 중 두 전구가 동시에 켜져 있던 시간은 몇 초일까?

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 네 개의 정수 A, B, C, D (0 ≤ A < B ≤ 100, 0 ≤ C < D ≤ 100)가
공백 하나를 사이로 두고 순서대로 주어진다.

[출력]
각 테스트 케이스마다, 두 전구가 동시에 켜져 있던 시간이 몇 초인지를 한 줄에 하나씩 출력한다.

3
1 3 5 7
0 5 2 4
0 5 1 6


#1 0
#2 2
#3 4

'''
ans_list = []

for test_case in range(1,1+int(input())):
    start_A, end_A, start_B, end_B = map(int, input().split(" "))
    # print(start_A, end_A, start_B, end_B)
    start_std, end_std = 0, 0
    if start_A >= start_B:
        start_std = start_A
    else: start_std = start_B
    if end_A >= end_B:
        end_std = end_B
    else: end_std = end_A

    ans = end_std - start_std

    if ans <= 0:
        ans = 0
        ans_list.append(ans)
    else: ans_list.append(ans)
num = 1
for i in ans_list:
    print(f'#{num} {i}')
    num += 1