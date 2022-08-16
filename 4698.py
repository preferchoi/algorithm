'''
삼성시는 버스 노선을 일반, 급행, 광역 급행으로 구분해 새롭게 바꾸려고 한다. 모든 정류장은 1번부터 1000번까지의 번호가 부여되어 있으며, 각 노선은 A에서 B번 정류장까지 다음 규칙에 따라 운행한다.
- 모든 버스는 A번에서 출발해 B번까지 운행하므로, A와 B정류장에는 반드시 정차한다.
- 일반버스는 A번부터 B번 사이의 모든 정류장에 정차한다.
- 급행 버스는 A가 짝수인 경우 A와 B 사이의 모든 짝수 번호 정류장에 정차하고, A가 홀수인 경우 A와 B사이의 모든 홀수 번호 정류장에 정차한다.
- 광역 급행 버스는 A가 짝수인 경우 A와 B 사이의 모든 4의 배수 번호 정류장에, A가 홀수인 경우 A와 B 사이의 3의 배수이면서 10의 배수가 아닌 번호 정류장에 정차한다.

버스의 종류와 출발 도착 정류장에 대한 정보가 주어질 때, 최대 몇 개의 노선이 같은 정류장에 정차하는지 알아내는 프로그램을 만들어보자.

[입력]
첫 줄에 테스트케이스의 개수 T가 주어진다. (1<=T<=1000)
다음 줄부터 각 테스트케이스 별로 첫 줄에 노선의 수 N이 주어지고(1<=N<=100), N개의 줄에 걸쳐 버스 타입 (1 일반, 2 급행, 3 광역 급행)과 출발 정류장 번호 A, 종점인 정류장 번호 B가 빈칸으로 구분되어 주어진다. (1<=A

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

1
3
1 2 5
2 3 10
3 2 9

'''

for tc in range(1, 1 + int(input())):
    road = [0 for _ in range(1001)]
    N = int(input())
    for _ in range(N):
        bus_type, start, end = map(int, input().split())
        if bus_type == 1:
            for i in range(start, end + 1):
                road[i] += 1

        if bus_type == 2:
            for i in range(start, end, 2):
                road[i] += 1

        if bus_type == 3:
            if not start % 2:
                for i in range(start, end, 4):
                    road[i] += 1
            else:
                for i in range(start, end):
                    if not i % 3 and i % 10:
                        road[i] += 1

    print(f'#{tc} {max(road)}')
