N_list = [list(range(1, 15)) for _ in range(15)]

for y in range(1, 15):
    for x in range(14):
        N_list[y][x] = sum(N_list[y-1][:x+1])

for tc in range(int(input())):
    a = int(input())
    b = int(input())

    print(N_list[a][b-1])

