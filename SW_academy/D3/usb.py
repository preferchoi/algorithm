# 0.8 0.5
# 두번 뒤집어서 꼽힐 확률
# 제대로 꼽을 확률 * 안꼽힐 확률 * 꼽힐 확률
# 0.8*0.5*0.5
# 한번 뒤집어서 꼽힐 확률
# 거꾸로 꼽을 확률 * 꼽힐 확률
# 0.2*0.5*0.5

for test in range(1, int(input())+1):
    pq = list(map(float, input().split(" ")))
    p, q = pq[0], pq[1]

    if p * (1-q) * q > (1-p) * q:
        print(f'#{test} YES')
    else:
        print(f'#{test} NO')