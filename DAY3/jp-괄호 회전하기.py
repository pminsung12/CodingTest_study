from collections import deque


def isright(rotated):
    """stack 활용 - 올바름판단"""
    q = rotated.copy()
    stack = []
    while q:
        p = q.popleft()

        # 여는괄호 : push
        if p in "({[":
            stack.append(p)

        # 닫는괄호
        else:
            # 올바름
            if stack and (
                (stack[-1] == "(" and p == ")")
                or (stack[-1] == "{" and p == "}")
                or (stack[-1] == "[" and p == "]")
            ):
                stack.pop()

            # 올바름X : empty or top is not 여는괄호
            else:
                return False
    return False if stack else True


def solution(s):

    rotated = deque(list(s))

    # 올바른괄호문자열 개수
    cnt = 0

    # 회전횟수 : 문자열개수까지
    n = 0

    while n < len(s):
        rotated.rotate(-1)  # 왼쪽회전
        cnt += 1 if isright(rotated) else 0
        n += 1
    return cnt
