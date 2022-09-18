# for tc in range(1, 1+ int(input()))

NM = input().split()
N, M = NM[0], NM[1]
if N == 1:
    if M == 2:
        print('B')
    else:
        print('A')
elif N == 2:
    if M == 3:
        print('B')
    else:
        print('A')
else:
    if N == 3:
        print('B')
    else:
        print('A')