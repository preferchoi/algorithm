N = int(input())
A, B = 3, 5
cnt = N // (A * B) * A

num_list = []
for five in range(N // A + 3):
    for three in range(N // B + 3):
        if five * 5 + three * 3 <= N:
            num_list.append([five * 5 + three * 3, five + three])
# print(num_list)
num_list.sort()
# print(num_list)

for i, j in num_list:
    if N == i:
        print(j)
        break
else:
    print(-1)

'''
최소공배수만큼 일단 제외하고 나머지에서 정리
 
'''
