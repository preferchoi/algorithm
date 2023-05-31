def put(item):
    queue.append(item)

def get():
    return queue.pop(0)

queue = []
put(1)
put(2)
put(3)
put(4)

print('현재 큐')
print(queue)

while queue:
    print(f'pop > {get()}')