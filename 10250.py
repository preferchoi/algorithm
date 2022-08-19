'''
2
6 12 10
30 50 72

'''

for tc in range(1, 1 + int(input())):
    H, W, num = map(int, input().split())

    print(f"{num % H}{'0' + str(num // H + 1) if num // H + 1 < 10 else num // H + 1}")
