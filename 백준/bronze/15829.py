n = int(input())
word = input()

cnt = 0

for i in range(n):
    cnt += (ord(word[i]) - 96) * (31 ** i)
print(cnt% 1234567891)
