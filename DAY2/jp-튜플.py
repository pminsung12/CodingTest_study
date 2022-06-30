import re


def solution(s):
    # 길이순으로 집합 정렬
    groups = sorted(
        list(map(lambda x: x[1:-1].split(","), re.findall("\{[\d,]+\}", s))), key=len
    )

    # 첫번째 집합으로 배열 초기화
    li = groups[0]

    # 집합 순회하며 새로운 원소 배열에 추가
    for g in groups[1:]:
        li += list(set(g) - set(li))

    return list(map(int, li))
