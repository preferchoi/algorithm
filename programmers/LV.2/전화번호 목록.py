def solution(phone_book):
    answer = True
    phone_book.sort()
    tmp = phone_book[0]
    for i in phone_book[1:]:
        if tmp == i[:len(tmp)]:
            answer = False
            break
        tmp = i
    return answer