'''
3
S01D02H03H04
H02H10S11H02
S10D10H10C01

'''
for tc in range(1, 1 + int(input())):
    s = input()
    deck = {'S': [], 'D': [], 'H': [], 'C': []}

    for i in range(0, len(s), 3):
        deck[s[i]].append(int(s[i + 1:i + 3]))

    flag = 1

    for i in deck.values():
        if len(i) != len(set(i)):
            flag = 0
            break

    print(f'#{tc}', end=' ')
    if flag:
        print(f'{13 - len(deck["S"])} {13 - len(deck["D"])} {13 - len(deck["H"])} {13 - len(deck["C"])}')
    else:
        print('ERROR')
