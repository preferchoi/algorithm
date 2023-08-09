def solution(id_list, report, k):
    answer = {key: 0 for key in id_list}

    report_check_from = {key: {key: 0 for key in id_list} for key in id_list}
    report_check_to = {key: {key: 0 for key in id_list} for key in id_list}

    for tmp in report:
        from_user, to_user = tmp.split()
        report_check_from[from_user][to_user] = 1
        report_check_to[to_user][from_user] = 1

    report_users = []
    for key, v in report_check_to.items():
        if sum(v.values()) >= k:
            report_users.append(key)

    for key, v in report_check_from.items():
        for tmp in report_users:
            answer[key] += v[tmp]
            
    tmp = [0 for _ in range(len(id_list))]
    
    for key, v in answer.items():
        tmp[id_list.index(key)] = v
    print(tmp)
    
    return tmp
