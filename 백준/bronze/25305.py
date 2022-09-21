'''
5 2
100 76 85 93 98

'''
N, k = map(int, input().split())
x_list = list(map(int, input().split()))
x_list.sort()
print(x_list[-k])
