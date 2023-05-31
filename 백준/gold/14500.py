'''
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

'''

Y, X = map(int, input().split())
base_lst = [list(map(int, input().split())) for _ in range(Y)]

sumV = []
for y in range(Y):
    for x in range(X):

        if x <= X - 4:
            sumV += [base_lst[y][x] + base_lst[y][x + 1] + base_lst[y][x + 2] + base_lst[y][x + 3]]
        if y <= Y - 4:
            sumV += [base_lst[y][x] + base_lst[y + 1][x] + base_lst[y + 2][x] + base_lst[y + 3][x]]

        if x <= X - 3 and y <= Y - 2:
            tmp = base_lst[y][x] + base_lst[y][x + 1] + base_lst[y][x + 2]
            sumV += [tmp + base_lst[y + 1][x]]
            sumV += [tmp + base_lst[y + 1][x + 1]]
            sumV += [tmp + base_lst[y + 1][x + 2]]
            tmp = base_lst[y + 1][x] + base_lst[y + 1][x + 1] + base_lst[y + 1][x + 2]
            sumV += [tmp + base_lst[y][x]]
            sumV += [tmp + base_lst[y][x + 1]]
            sumV += [tmp + base_lst[y][x + 2]]
            sumV += [base_lst[y][x] + base_lst[y][x + 1] + base_lst[y + 1][x + 1] + base_lst[y + 1][x + 2]]
            sumV += [base_lst[y][x + 1] + base_lst[y][x + 2] + base_lst[y + 1][x] + base_lst[y + 1][x + 1]]

        if x <= X - 2 and y <= Y - 3:
            tmp = base_lst[y][x] + base_lst[y + 1][x] + base_lst[y + 2][x]
            sumV += [tmp + base_lst[y][x + 1]]
            sumV += [tmp + base_lst[y + 1][x + 1]]
            sumV += [tmp + base_lst[y + 2][x + 1]]
            tmp = base_lst[y][x + 1] + base_lst[y + 1][x + 1] + base_lst[y + 2][x + 1]
            sumV += [tmp + base_lst[y][x]]
            sumV += [tmp + base_lst[y + 1][x]]
            sumV += [tmp + base_lst[y + 2][x]]
            sumV += [base_lst[y][x] + base_lst[y + 1][x] + base_lst[y + 1][x + 1] + base_lst[y + 2][x + 1]]
            sumV += [base_lst[y][x + 1] + base_lst[y + 1][x + 1] + base_lst[y + 1][x] + base_lst[y + 2][x]]

        if x <= X - 2 and y <= Y - 2:
            sumV += [base_lst[y][x] + base_lst[y + 1][x] + base_lst[y][x + 1] + base_lst[y + 1][x + 1]]

print(max(sumV))
