from itertools import combinations

N = int(input())
base_lst = [list(map(int, input().split())) for i in range(N)]
players = list(range(N))

All_team = list(combinations(players, N // 2))
key = len(All_team) // 2
team_A, team_B = All_team[:key], All_team[key:]
team_B.reverse()
minV = 9999

for i in range(key):
    sumV = 0
    for p_1 in team_A[i]:
        for p_2 in team_A[i]:
            sumV += base_lst[p_1][p_2]

    for p_1 in team_B[i]:
        for p_2 in team_B[i]:
            sumV -= base_lst[p_1][p_2]
    if minV > abs(sumV):
        minV = abs(sumV)
print(minV)
