'''
1
2
1 3
2 5
5
1
2
3
4
5

'''
global station_list
global list_count

def stop(s_num, e_num, station_list, list_count):
    web = list(range(s_num, e_num + 1))
    for i in range(len(station_list)):
        if station_list[i] in web:
            list_count[i] += 1

for test_case in range(1, 1+int(input())):
    N = int(input())
    bus_list = []
    for i in range(N):
        bus_list.append(list(map(int, input().split(" "))))
    P = int(input())
    station_list = []
    for i in range(P):
        station_list.append(int(input()))

    list_count = [0]*P

    for i, j in bus_list:
        stop(i, j, station_list, list_count)

    print(f'#{test_case}', end=" ")
    for i in list_count:
        print(i, end = " ")
    print()