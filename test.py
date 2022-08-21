a = input()
b = input()

flag = 1
if len(a) == len(b):  # 문장 길이 같음
    for i in range(len(a)):
        if a[i] != b[i]:  # 인덱스끼리 비교
            flag = 0

else:
    flag = 0

if flag == 1:
    print('같음')

else:
    print('다름')
