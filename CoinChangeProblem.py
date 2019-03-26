A = [1, 2, 3]
total = 4

# dynamic programming solution to coin change problem
# to find the minimum number of coins required to make total from change
def coin_change(total, A):
    dp = [[0 for _ in range(total+1)] for __ in range(len(A)+1)]

    for i in range(len(A)+1):
        for j in range(total+1):
            if i == 0:
                continue
            elif j < A[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-A[i-1]])

    print(dp)
    return dp[len(A)][total]


print(coin_change(total, A))


# DFS recursion function to find combinations of numbers in array

globalList = []
def findListCountDFS(currentList):
    global A
    global globalList
    currentSum = sum(currentList)
    if currentSum > total:
        return 0
    elif currentSum == total:
        # print(currentList," = ",str(currentSum))
        globalList.append(currentList)
    elif currentSum < total:
        for j in A:
            nextList = currentList + [j]
            # print(nextList)
            findListCountDFS(nextList)


for i in A:
    currentList = [i]
    if i <= total:
        findListCountDFS(currentList)

globalSet = set()
# print('globalList =',globalList)
for perlist in globalList:
    globalSet.add(tuple(sorted(perlist)))
print('globalSet =', globalSet)
print('count = ', len(globalSet))
