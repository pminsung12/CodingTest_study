from collections import deque


def flip(u):
    # 처음, 마지막 원소 제거
    u.popleft()
    u.pop()

    # flip
    res = "".join(["(" if p == ")" else ")" for p in u])
    return res


def isright(u):
    # 올바름 검사
    stack = []
    for p in u:
        if p == "(":
            stack.append(p)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return False if stack else True


def recur(v):

    # 빈문자열 처리
    if not v:
        return ""

    u = deque([])
    cnt = 0

    while True:
        p = v.popleft()

        if p == "(":
            cnt -= 1
        else:
            cnt += 1

        u.append(p)

        # 균형: u
        if cnt == 0:
            # 올바름
            if isright(u):
                return "".join(u) + recur(v)
            else:
                return "(" + recur(v) + ")" + flip(u)


def solution(s):
    v = deque(list(s))
    return recur(v)
