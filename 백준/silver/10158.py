w, h = map(int, input().split())
now_x, now_y = map(int, input().split())
t = int(input())

t_x = t + now_x
t_y = t + now_y
ans_x = t_x % (w * 2)
ans_y = t_y % (h * 2)

if ans_y > h:
    ans_y = h * 2 - ans_y

if ans_x > w:
    ans_x = w * 2 - ans_x

print(ans_x, ans_y)
# go_y, go_x = 1, 1
# cnt = 0
# cnt_x, cnt_y = 0, 0
# time = 0
#
# while time < t:
#     if go_y > 0:
#         y = h - now_y
#     else:
#         y = now_y
#     if go_x > 0:
#         x = w - now_x
#     else:
#         x = now_x
#
#     if y > x:
#         now_y += x * go_y
#         now_x += x * go_x
#         time += x
#         if time < t:
#             go_x *= -1
#     elif y < x:
#         now_y += y * go_y
#         now_x += y * go_x
#         time += y
#         if time < t:
#             go_y *= -1
#     else:
#         now_y += y * go_y
#         now_x += x * go_x
#         time += y
#         if time < t:
#             go_y *= -1
#             go_x *= -1
#
# now_y -= go_y * (time - t)
# now_x -= go_x * (time - t)
# print(now_x, now_y)
