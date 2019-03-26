def subset_sum(total, nums):

    dp = [[False for _ in range(total+1)] for __ in range(len(nums)+1)]
    dp[0][0] = True
    for i in range(1,len(nums)+1):
        for j in range(total+1):
            if j == 0:
                dp[i][j] = True
            elif j < nums[i-1]:
                dp[i][j] = dp[i-1][j]
            elif dp[i-1][j]:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i-1][j-nums[i-1]]

    return dp[len(nums)][total]


total = 11
nums = [2,3,7,8,10]

print(subset_sum(total,nums))
