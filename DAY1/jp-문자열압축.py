def solution(s):

    # 문자열길이
    n = len(s)
    minval = float("inf")

    if n == 1:
        return 1

    for window in range(1, n // 2 + 1 + 1):  # window 변화

        short = ""
        unit = ""
        cnt = 0

        for idx in range(0, n + 1, window):  # window로 문자열 순회

            if unit == "":
                unit = s[idx : idx + window]
                cnt += 1
            else:
                if s[idx : idx + window] == unit:
                    cnt += 1
                else:
                    short += str(cnt) + unit if cnt > 1 else unit
                    unit = s[idx : idx + window]
                    cnt = 1

        # 마지막 남은 문자열 존재 시
        if cnt == 1:
            short += unit
        minval = min(len(short), minval)

    return minval
