L = int(input())
s = input()
N = len(s)
minV = L // N
ans = minV - 2
for i in range(N):
    if s[:i+1]+s[i:] != s:
        tmp = (L + i) // N - 1
        if minV > tmp:
            minV = tmp
            if minV == ans:
                break
print(minV)



'''
8
asdf
'asdf''asdf'
sdf'asdf'a
df'asdf'as
f'asdf'asd

10
aad
'aad''aad''aad'a

7
asda
sda'asda'
da'asda'a
'asda'asd

5
aaaaa

13
안녕하세요
안녕하세요안녕하세요안녕하
녕하세요'안녕하세요'안녕하세
'''
