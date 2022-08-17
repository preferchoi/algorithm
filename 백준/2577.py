sumV = 1
for _ in range(3):
    sumV *= int(input())
ans_list = [0 for _ in range(10)]
while sumV:
    ans_list[sumV % 10] += 1
    sumV //= 10
for i in ans_list:
    print(i)