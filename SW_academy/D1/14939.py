def inner():
    for i in range(len(str2)):
        if str2[i:i+len_str1] == str1:
            return 1
    return 0

for tc in range(1, 1 + int(input())):
    str1 = input()
    str2 = input()
    len_str1 = len(str1)
    len_str2 = len(str2)

    print(f'#{tc} {inner()}')
