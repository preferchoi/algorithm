def solution(park, routes):
    answer = []
    limit = len(park)
    y_limit, x_limit = len(park), len(park[0])
    y = 0
    flag = False
    for i in park:
        x = 0
        for j in i:
            if j == 'S':
                flag = True
                break
            x += 1
        if flag:
            break
        y += 1
    
    park[y] = park[y].replace('S','O')
    
    delta = {'E':(0, 1), 'W':(0, -1), 'S':(1, 0), 'N':(-1, 0)}
    
    for route in routes:
        arrow, num = route.split(' ')
        dy, dx = y, x
        for i in range(int(num)):
            dy += delta[arrow][0]
            dx += delta[arrow][1]
            if 0 <= dy < y_limit and 0 <= dx < x_limit:
                if park[dy][dx] == 'X':
                    dy, dx = y, x
                    break
            else:
                dy, dx = y, x
                break
        y, x = dy, dx
            
    return y, x