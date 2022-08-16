'''
2

() (  (  ( () ()  )  ( () ) () )  ) (  ()  )
L p1 p2 p3 L  L  p3 p4 L p4 L p2 p1 p5 L p5
(((()(()()))(())()))(()())


2
()(((()())(())()))(())
(((()(()()))(())()))(()())

'''

for tc in range(1, 1 + int(input())):
    s = input()
    s_list = list(s.replace('()', 'L'))

    patition = 0
    ans = 0
    for i in s_list:
        if i == '(':
            patition += 1
        if i == ')':
            patition -= 1
            ans += 1
        if i == 'L':
            ans += patition
    print(f'#{tc} {ans}')