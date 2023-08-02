def solution(today, terms, privacies):
    answer = []
    
    year_limit, month_limit = 12, 28
    # print(today, terms, privacies)
    rules = dict()
    for s in terms:
        title, content = s.split(' ')
        rules[title] = int(content)
    # print(rules)
    
    today_y, today_m, today_d = map(int, today.split('.'))
    
    for i in range(len(privacies)):
        day, rule = privacies[i].split(' ')
        day_y, day_m, day_d = map(int, day.split('.'))
        # print(rules[rule])
        day_y += rules[rule]//12
        day_m += rules[rule]%12
        day_y += day_m//12
        day_m %= 12
        day_d -= 1
        
        if day_d == 0:
            day_d = 28
            day_m -= 1
        if day_m <= 0:
            day_m += 12
            day_y -= 1

        
        print(day_y, day_m, day_d, rule)
        flag = False
        if day_y < today_y:
            flag = True
        elif day_y == today_y:
            if day_m < today_m:
                flag = True
            elif day_m == today_m:
                if  day_d < today_d:
                    flag = True
        if flag:
            answer.append(i+1)
    return answer