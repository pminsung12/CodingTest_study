def solution(record):

    answer = []
    uid2name = {r.split()[1]: r.split()[2] for r in record if r.split()[0] != "Leave"}

    for r in record:

        info = r.split()

        if info[0] != "Leave":
            act, uid, name = info
        else:
            act, uid = info

        if act == "Enter":
            msg = f"{uid2name[uid]}님이 들어왔습니다."
            answer.append(msg)

        elif act == "Leave":
            msg = f"{uid2name[uid]}님이 나갔습니다."
            answer.append(msg)

        else:
            continue

    return answer
