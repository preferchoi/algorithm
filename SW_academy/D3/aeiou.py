'''
3
congratulation
synthetic
fluid
'''
T = int(input())

for test in range(1, T+1):
    string = input()
    print(f'#{test}', end=" ")
    for i in string:
        if i != "a" and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            print(i, end="")
    print()