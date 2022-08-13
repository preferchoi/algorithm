'''
2
cat
dog
man
mana

'''
for tc in range(1, 1 + int(input())):
    s1 = input().strip()
    s2 = input().strip()

    l_1 = len(s1)
    l_2 = len(s2)
    if l_1 == l_2:
        if ord(s1[-1]) - ord(s2[-1]) == -1 and s1[:l_1-1] == s2[:l_2-1]:
            print(f'#{tc} N')
        else:
            print(f'#{tc} Y')
    else:
        if l_1 - l_2 == -1:
            if s1 == s2[l_2-1] and s2[-1] == 'a':
                print(f'#{tc} Y')
            else:
                print(f'#{tc} N')
        else:
            print(f'#{tc} N')
