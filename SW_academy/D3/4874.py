'''
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .

(num) (num) (oper) 구조일 때만 연산이잖아
1 5 8 10 3 4 + + 3 + * 2 + + + .의 경우
[+ + 3 + * 2 + + + .]
[1 5 8 10 3 4]
까지는 걍 집어넣음
[+ 3 + * 2 + + + .]
[1 5 8 10 3 4 +]가 되면
연산해서
[+ 3 + * 2 + + + .]
[1 5 8 10 7] 로 만들고
[3 + * 2 + + + .]
[1 5 8 10 7 +]니까 또 연산해서
[3 + * 2 + + + .]
[1 5 8 17]로 될거고
[+ * 2 + + + .]
[1 5 8 17 3] 되고
[* 2 + + + .]
[1 5 8 20]
[2 + + + .]
[1 5 160]
[+ + + .]
[1 5 160 2]
[1 5 162] -> [1 167] -> [168]이 되는거지

10 2 + 3 4 + *
스택에 맨 뒤부터 집어넣자
[10, 2, +, 3, 4, +]
[*]
[10, 2, +, 3, 4]
[*, +]
[10, 2, +, 3]
[*, +, 4]
[10, 2, +]
[*, +, 4, 3] ----> 4 + 3 = 7
[10, 2, +]
[*, 7]
[10, 2]
[*, 7, +]
[10]
[*, 7, +, 2]
[]
[*, 7, +, 2, 10] ----> 2 + 10 = 12
[]
[*, 7, 12] ----> 7 * 12 = 84
[]
[84]

'''
for tc in range(1, 1 + int(input())):
    quest = list(input().split())
    # print(quest)
    stack = []
    now = None
    try:
        while True:
            now = quest.pop(0)
            # 위에서 . 없으면 알아서 터져서 except하잖아
            if now == '.':
                break
            # 그러면 여기서는 . 나와서 정상적으로 끝내주는거고

            if now not in ['+', '*', '-', '/']:
                stack.append(int(now))
            else:
                oper = now
                if oper == '+':
                    stack.append(stack.pop() + stack.pop())
                elif oper == '*':
                    stack.append(stack.pop() * stack.pop())
                elif oper == '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif oper == '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b // a)

        if len(stack) == 1:
            # 스택에 숫자 한개 남아있고 끝나면 그거 보여주고
            print(f'#{tc} {stack.pop()}')
        else:
            # 스택 비어있거나 두개이상 들어있으면 연산 이상한거니까 error 해주고
            print(f'#{tc} error')
    except Exception:
        # 위에서 무한루프돌거같으면, 예를들어 '.'이 없으면, 스택에서 뽑아올게 없으면 인덱스에러나서 그냥 error 내보내주고
        print(f'#{tc} error')
