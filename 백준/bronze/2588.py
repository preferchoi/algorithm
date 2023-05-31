N = int(input())
M = input()

ans_list = []
for i in M:
    ans_list.append(int(i) * N)
print(ans_list.pop())
print(ans_list.pop())
print(ans_list.pop())
print(int(M) * N)