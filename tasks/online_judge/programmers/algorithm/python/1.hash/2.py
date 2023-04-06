def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        curr = phone_book[i]
        phone_book.pop(i)
        if any(phone.startswith(curr) for phone in phone_book):
            answer = False
            break
        phone_book.insert(i, curr)
    return answer