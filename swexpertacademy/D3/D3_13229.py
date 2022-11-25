week = {6: 'MON', 5: 'TUE', 4: 'WED', 3: 'THU', 2: 'FRI', 1: 'SAT', 7: 'SUN'}

for test_case in range(1, int(input())+1):
    Q = input()
    for i in week:
        if Q == week[i]:
            print(f'#{test_case} {i}')
