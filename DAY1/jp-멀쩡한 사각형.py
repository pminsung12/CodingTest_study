def gcd(w, h):
    a, b = w, h
    while True:
        r = a % b
        if r == 0:
            return b
        a, b = b, r


def solution(w, h):
    print(gcd(12, 8))
    return w * h - (w + h - gcd(w, h))
