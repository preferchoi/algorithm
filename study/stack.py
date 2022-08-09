def put(item):
    stack.append(item)

def get():
    return stack.pop()

stack = []
put(1)
put(2)
put(3)
put(4)

print('현재 스택')
print(stack)

while stack:
    print(f'pop > {get()}')