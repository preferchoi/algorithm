def solution(dirs):
    answer = 0
    ref = set()
    
    nowX, nowY = 0,0
    for command in dirs:
        if command == 'U' and nowY < 5:
            ref.add(f'{nowX, nowY, nowX, nowY+1}')
            nowY = nowY+1
        elif command == 'D' and nowY > -5:
            ref.add(f'{nowX, nowY-1, nowX, nowY}')
            nowY = nowY-1
        elif command == 'R' and nowX < 5:
            ref.add(f'{nowX, nowY, nowX+1, nowY}')
            nowX = nowX+1
        elif command == 'L' and nowX > -5:
            ref.add(f'{nowX-1, nowY, nowX, nowY}')
            nowX = nowX-1
    
    return len(ref)