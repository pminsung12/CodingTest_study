def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
            continue
        stack.append(c)
    return 0 if stack else 1


def solution(s):
    """초기버전"""
    stack = []
    for c in s:
        if stack:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)

    return 0 if stack else 1
