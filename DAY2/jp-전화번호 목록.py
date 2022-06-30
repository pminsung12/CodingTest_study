# 정렬 + startwith : O(nlogn)
def solution(phoneBook):
    # 문자열 정렬 : 앞 원소가 뒤에 원소에 포함되는지만 check
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


# hash 풀이
def solution(phone_book):
    d = {}
    for phone_number in phone_book:
        d[phone_number] = 1

    for number in phone_book:
        prefix = ""
        for s in number:
            prefix += s
            if prefix in d and prefix != number:
                return False
    return True
