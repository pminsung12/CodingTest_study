def solution(n):

	# dp[1], dp[2] 미리 연산
	dp = [0] + [1] + [2] + [0 for _ in range(70000)]

	# dp[n] = dp[n-1]에서 1을 붙이는 경우 + dp[n-2]에서 2를  붙이는 경우
	for i in range(3, n+1):
		dp[i] = (dp[i-1] + dp[i-2]) %1000000007

	return dp[n]