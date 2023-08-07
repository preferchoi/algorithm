def solution(wallpaper):
    answer = []
    sy, sx, ey, ex = 0, 0, 0, 0
    
    for y in range(len(wallpaper)):
        if "#" in wallpaper[y]:
            sy = y
            break
    
    for y in range(len(wallpaper)-1, -1, -1):
        if "#" in wallpaper[y]:
            ey = y + 1
            break
    
    x_wallpaper = [[] for _ in range(len(wallpaper[0]))]
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            x_wallpaper[x].append(wallpaper[y][x])
    
    for x in range(len(x_wallpaper)):
        if "#" in x_wallpaper[x]:
            sx = x
            break
    
    for x in range(len(x_wallpaper)-1, -1, -1):
        if "#" in x_wallpaper[x]:
            ex = x + 1
            break
    
    return sy, sx, ey, ex