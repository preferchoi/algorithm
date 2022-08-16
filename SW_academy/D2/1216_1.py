'''
12345
n = (N -1, -1, -1) m = (0, N-n)
12345   N = 5 M = 0

1234    N = 4 M = 0
 2345   M = 1

123     N = 3 M = 0
 234    M = 1
  345   M = 2

12      N = 2 M = 0
 23     M = 1
  34    M = 2
   45   M = 3

1       N = 1 M = 0
 2      M = 1
  3     M = 2
   4    M = 3
    5   M = 4
'''


def check_x(word_list):
    for len_key in range(N, -1, -1):  # 99>98>97>96>95>94...5>4>3>2>1>0
        for x in range(N):  # 0>1>2>3>4...96>97>98>99
            for y in range(N - len_key + 1):  # 0>[0,1]>[0,1,2]>[0,1,2,3]>[0,1,2,3,4]>...[0,1,2,3,...94,95,96,97,98,99]
                if word_list[x][y:y + len_key-1] == word_list[x][y + len_key - 1:y:-1]:  #
                    return len_key, len(word_list[x][y:y+len_key])


def check_y(word_list):
    for len_key in range(N, -1, -1):  # 99>98>97>96>95>94...5>4>3>2>1>0
        for x in range(N):  # 0>1>2>3>4...96>97>98>99
            for y in range(N - len_key):  # 0>[0,1]>[0,1,2]>[0,1,2,3]>[0,1,2,3,4]>...[0,1,2,3,...94,95,96,97,98,99]
                y_set = []
                for y_q in range(y, y + len_key):
                    y_set.append(word_list[y_q][x])

                if y_set == y_set[::-1]:
                    return len_key


for tc in range(1, 11):
    N = int(input())
    N = 100
    word_list = [list(input()) for _ in range(N)]

    rx, lx = check_x(word_list)
    ry = check_y(word_list)
    print(f'#{tc} {rx if rx > ry else ry}')
