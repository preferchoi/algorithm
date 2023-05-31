N = int(input())
stack = []
for _ in range(N):
    s = int(input())
    if s:
        stack.append(s)
    else:
        stack.pop()
print(sum(stack))
