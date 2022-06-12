def solution(n):
	numbers = [4,1,2]
	a = n
	li = []
	while a!=0:
		a, r = divmod(a, 3)
		a -= (r==0)
		li.append(numbers[r])
	return ''.join(map(str, li[::-1]))