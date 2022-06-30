from collections import deque


def solution(bridge_length, weight, truck_weights):

    # 다리위, 대기트럭 : 큐 사용
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)

    # 다리 위 무게합
    wsum = 0

    # 소요시간
    ans = 0

    while bridge:

        # 1초 경과 : front pop
        ans += 1
        wsum -= bridge.popleft()

        if truck_weights:

            # 트럭 추가 (용량이하)
            if wsum + truck_weights[0] <= weight:
                w = truck_weights.popleft()
                bridge.append(w)
                wsum += w

            # 용량초과 : 자리만 채움
            else:
                bridge.append(0)

    return ans
