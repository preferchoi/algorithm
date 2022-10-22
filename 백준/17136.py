base_lst = [list(map(int, input().split())) for _ in range(10)]

ans = [0] * 6
for y in range(10):
    for x in range(10):
        if base_lst[y][x] == 1:
            for cell in range(5, 0, -1):
                if y + cell <= 10 and x + cell <= 10:
                    flag = True
                    for cell_y in range(cell):
                        if sum(base_lst[y + cell_y][x:x + cell]) != cell:
                            flag = False
                            break
                    if flag:
                        ans[cell] += 1
                        for cell_y in range(cell):
                            for cell_x in range(cell):
                                base_lst[y+cell_y][x+cell_x] = 0
                        for i in base_lst:
                            print(*i)
print(ans)
for i in ans:
    if i > 5:
        print(-1)
        break
else:
    print(sum(ans))