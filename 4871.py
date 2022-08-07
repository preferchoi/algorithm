'''
3
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

1
6 5
1 4
1 3
2 3
2 5
4 6
1 6

'''
for tc in range(1, 1 + int(input())):
    V, E = map(int, input().split())
    mapp = [[False for _ in range(V)] for _ in range(V)]

    for i in range(E):
        start, end = map(int, input().split())
        start, end = start - 1, end - 1
        mapp[start][end] = True

    quest_start, quest_end = map(int, input().split())
    quest_start, quest_end = quest_start - 1, quest_end - 1
    stack = [quest_start]
    
    try:
        while True:
            quest_start = stack.pop()
            if quest_start == quest_end:
                break
            for i in range(V):
                if mapp[quest_start][i]:
                    stack.append(i)
        print(f'#{tc} 1')
    except IndexError:
        print(f'#{tc} 0')
'''
[[False, False, True, True, False, False],
 [False, False, True, False, True, False],
 [False, False, False, False, False, False],
 [False, False, False, False, False, True],
 [False, False, False, False, False, False],
 [False, False, False, False, False, False]]
 
 quest_start, quest_end = 0, 5일 때
 
 mapp[quest_start], 즉 mapp[0]의 내부 요소 체크
 [F, F, T, T, F, F]
 
 체크하면서 T일 경우 quest_start를 T 인덱스 값으로 바꿔주고, 그 요소는 F로 변경
 quest_start가 2로 변경됨
 mapp[quest_start], 즉 mapp[2]의 내부 요소 체크
 [F, F, F, F, F, F]
 
 모든 요소가 F, 다음 노드로 이동할 수 없으니 qeust_start를 이전 노드로 이동시킴
 
 mapp[quest_start], 즉 mapp[0]의 내부 요소 체크
 [F, F, F, T, F, F]
 
 체크하면서 T일 경우 quest_start를 T 인덱스 값으로 바꿔주고, 그 요소는 F로 변경
 quest_start가 3으로 변경됨
 
 mapp[quest_start], 즉 mapp[3]의 내부 요소 체크
 [F, F, F, F, F, T]
 
 체크하면서 T일 경우 quest_start를 T 인덱스 값으로 바꿔주고, 그 요소는 F로 변경
 quest_start가 5으로 변경됨
 
 mapp[quest_start], 즉 mapp[5]의 내부 요소 체크
 하기 전에, quest_start가 quest_end와 같아졌기 때문에 while루프 종료
 
 이게 맞지
 이걸 스택으로?
 굳이 T를 F로 바꾸지 말고 이동 가능한 경로를 상위 노드부터 돌리는거임
 1번부터 돌린다 쳤을 때, [2, 3]이 되는거고 이제 pop() 해서 맨 뒤에 4 뽑은 다음에 4에서 가능한 경로 뽑아서 스택에 추가하면?
 현재 스택은 [2, 5] 그 뒤에 pop() 해서 quest_end랑 비교해서 같으니까 가능하다고 출력 
 만약 현재 노드에서 갈 수 있는데가 없으면 한층 올라가서 다음 칸으로 내려가면 되는거고
'''