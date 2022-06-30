from itertools import permutations


def solution(numbers):
    # 소수 순열 경우의 수 - 0, 1 제외
    ans = set()
    for k in range(1, len(numbers) + 1):
        ans.update(set(map(int, map("".join, permutations(numbers, k)))))
    ans -= set([0, 1])

    # 에라토스테네스의 체
    for i in range(2, int(max(ans) ** 0.5) + 1):
        ans -= set([j for j in range(i * 2, max(ans) + 1, i)])

    return len(ans)
