from itertools import combinations as cmb
from collections import Counter


def solution(relation):
    ncol = len(relation[0])

    # 모든 속성 조합 (combinations)
    combinations = []
    for i in range(1, ncol + 1):
        combinations += cmb(range(ncol), i)

    cand = []

    for comb in combinations:

        # 새로운 릴레이션 : 튜플 재구성 (컬럼조합)
        new_rel = [" ".join([tuple[colidx] for colidx in comb]) for tuple in relation]

        # 유일성 check (중복존재X)
        if Counter(new_rel).most_common(1)[0][1] == 1:
            # if set(new_rel) == nrow: # nrow = len(relation)

            # 후보키 여부
            flag = True

            # 최소성 여부 : 후보키가 포함된 속성 조합 제외
            for c in cand:
                if set(c).subset(set(comb)):
                    flag = False
                    break

            if flag:
                cand.append(comb)

    return len(cand)
