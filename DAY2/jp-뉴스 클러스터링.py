import re

def solution(s1, s2):
	# 알파벳으로 이루어진 2음절 배열 생성
	li1 = [s1[i:i+2].upper() for i in range(len(s1)-1) if re.match("[a-zA-Z]{2}", s1[i:i+2])] 
	li2 = [s2[i:i+2].upper() for i in range(len(s2)-1) if re.match("[a-zA-Z]{2}", s2[i:i+2])] 
	# if not re.findall('[^a-zA-Z]+', str1[i:i+2])
	
	# 둘다 empty면 종료
	if not li1 and not li2:
		return 1*65536

	# 모든 2음절 조합 배열 생성
	allbi = set(li1)|set(li2)

	# 교집합은 min, 합집합은 max count로 count
	inter = [min(li1.count(bigram), li2.count(bigram)) for bigram in allbi]
	union = [max(li1.count(bigram), li2.count(bigram)) for bigram in allbi]

	# 자카드 유사도 계산	
	jac = sum(inter)/sum(union)
	
	return int(jac*65536)