# BFS : 각 idx의 숫자에 1 또는 -1을 곱해서 더해보며 BFS
from collections import deque


def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque([(numbers[0], 1), (-numbers[0], 1)])

    while q:
        res, curr = q.popleft()
        if curr < n:
            for i in [1, -1]:
                q.append((res + numbers[curr] * i, curr + 1))
        else:
            if res == target:
                answer += 1

    return answer


# DFS(while)
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    stack = [(numbers[0], 1), (-numbers[0], 1)]

    while stack:
        res, curr = stack.pop()
        if curr < n:
            for i in [1, -1]:
                stack.append((res + numbers[curr] * i, curr + 1))
        else:
            if res == target:
                answer += 1

    return answer


# DFS(재귀)
def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(res, curr):
        nonlocal answer
        if curr >= n:
            if res == target:
                answer += 1
            return

        for i in [1, -1]:
            dfs(res + numbers[curr] * i, curr + 1)

    dfs(numbers[0], 1)
    dfs(-numbers[0], 1)
    return answer
