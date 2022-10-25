for tc in range(1, 1+ int(input())):
    word = list(input())
    r_word = word.copy()
    r_word.reverse()
    if word == r_word:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
