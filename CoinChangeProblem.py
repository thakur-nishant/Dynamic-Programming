A = [1,2,3]
total = 4

globalList = []

#recursion function to find combinations of numbers in array
def findListCount(currentList):
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
            findListCount(nextList)

for i in A:
    currentList = [i]
    if i <= total:
        findListCount(currentList)


globalSet = set()
# print('globalList =',globalList)
for perlist in globalList:
    globalSet.add(tuple(sorted(perlist)))
print('globalSet =',globalSet)
print('count = ', len(globalSet))



