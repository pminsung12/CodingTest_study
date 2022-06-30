from itertools import permutations as pm


def findShortestPath(name, src, trg):
    """
    idx_1 idx_3 간 최소거리:

    0 1 2 3 4
    v   v

    1 2 3 4 5
    v   v

    1 2 3 4 5 1 2
        v     v
    좌측이동 : len + (left+1) - (right+1)
    우측이동 : right+1 - (left+1)
    """
    left, right = sorted([src, trg])
    toright = right + 1 - (left + 1)
    toleft = len(name) + (left + 1) - (right + 1)
    return min(toright, toleft)


def solution(name):
    # 상하 이동횟수
    updown = sum([min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name])

    # 좌우 이동지점 : 시작위치, A 제외
    notA = [idx for idx in range(len(name)) if name[idx] != "A" and idx != 0]

    # 좌우이동 순열 경우의수
    cases = pm(notA, len(notA))

    # 좌우 이동횟수
    cost = float("inf")

    # 좌우 최소이동 계산
    for path in cases:
        src = 0
        dist = 0
        for trg in path:
            dist += findShortestPath(name, src, trg)
            src = trg
        cost = min(cost, dist)

    # 좌우 + 상하 이동횟수
    cnt += updown

    return cnt
