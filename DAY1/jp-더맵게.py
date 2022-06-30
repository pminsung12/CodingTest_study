import heapq as hq


def solution(scoville, k):

    hq.heapify(scoville)

    if sum(scoville) == 0:
        return -1

    cnt = 0
    while True:

        if scoville[0] >= k:
            return cnt

        if len(scoville) < 2:
            return -1

        s1 = hq.heappop(scoville)
        s2 = hq.heappop(scoville)

        s3 = s1 + s2 * 2

        cnt += 1

        hq.heappush(scoville, s3)
