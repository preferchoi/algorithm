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
                if len(stack) < 2:
                    stack = []
                    break
                stack.append(now)
            # 지들 타입 맞춰서 숫자랑 연산자 구분해서 추가할거고
            if len(stack) >= 3 and (type(stack[-3]) == int and type(stack[-2]) == int and type(stack[-1]) == str):
                # 최소기준은 길이 3 이상일 때, 그래야 숫자 숫자 연산자 들어갈 수 있으니까, 그 뒤에 숫자 숫자 연산자 구조인지 확인하고
                oper = stack.pop()
                # 연산자 뽑아주고
                if oper == '+':
                    stack.append(stack.pop() + stack.pop())
                elif oper == '*':
                    stack.append(stack.pop() * stack.pop())
                elif oper == '-':
                    stack.append(stack.pop() - stack.pop())
                elif oper == '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b // a)
                # 여기서 연산을 때려버리는거지
                # 하고 이제 반복
        if len(stack) == 1:
            # 스택에 숫자 한개 남아있고 끝나면 그거 보여주고
            print(f'#{tc} {stack.pop()}')
        else:
            # 스택 비어있거나 두개이상 들어있으면 연산 이상한거니까 error 해주고
            print(f'#{tc} error')
    except IndexError:
        # 위에서 무한루프돌거같으면, 예를들어 '.'이 없으면, 스택에서 뽑아올게 없으면 인덱스에러나서 그냥 error 내보내주고 
        print(f'#{tc} error')
        
    # 이론상문제없는데 왜 안되냐고ㅗㅗㅗㅗㅗㅗ뻐규머겅두번머겅