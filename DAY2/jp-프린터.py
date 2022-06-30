from collections import deque


def solution(priorities, location):
    # (문서번호, 중요도) 배열 생성
    q = deque([(idx, p) for idx, p in enumerate(priorities)])

    # 출력횟수
    cnt = 0

    while q:
        # 현재문서번호, 중요도
        curr, cp = q.popleft()
        pushed = False
        for _, p in q:

            # 중요도 큰 문서 존재 시 맨 뒤에 push (출력X)
            if cp < p:
                q.append((curr, cp))
                pushed = True
                break

        # 출력했을 경우
        if not pushed:
            cnt += 1
            if curr == location:
                return cnt
