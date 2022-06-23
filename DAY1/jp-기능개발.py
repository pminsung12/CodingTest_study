from math import ceil
def solution(progresses, speeds):
	taken = [ceil((100-p)/s) for p, s in zip(progresses, speeds)]
	answer = []
	curr_idx, curr = 0, taken[0]
	
	for after_idx, after in enumerate(taken):
		if after > curr:
			answer.append(after_idx-curr_idx)
			curr_idx = after_idx
			curr = after
	
	# 마지막개수 추가
	answer.append(len(taken) - curr_idx)
	return answer