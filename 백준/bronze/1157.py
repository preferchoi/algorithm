s = input()
dict_abc = {}
for i in s:
    i = i.upper()
    if i in dict_abc:
        dict_abc[i] += 1
    else:
        dict_abc[i] = 1
maxV = 0
ans = ''
for key, value in dict_abc.items():
    if value > maxV:
        maxV = value
        ans = key
    elif value == maxV:
        ans += key
if len(ans) == 1:
    print(ans)
else:
    print('?')