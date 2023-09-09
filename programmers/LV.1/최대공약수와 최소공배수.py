def solution(n, m):
    answer = []
    tmp1, tmp2 = [i for i in range(1,n//2+1) if n%i==0], [i for i in range(1,m//2+1) if m%i==0]
    tmp1.append(n)
    tmp2.append(m)
    for i in tmp1[::-1]:
        if i in tmp2:
            answer.append(i)
            break
    
    tmp3, tmp4 = n, m
    
    while tmp3 != tmp4:
        if tmp3 < tmp4:
            tmp3 += n
        else:
            tmp4 += m
    else:
        answer.append(tmp4)
    return answer