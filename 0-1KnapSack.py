def knapSack(total_weight, item_weight, item_value):
    n = len(item_value)
    K = [[0 for x in range(total_weight + 1)] for x in range(n + 1)]
    # print(K)
    # K = [[0] * (total_weight + 1)] * (n + 1)
    # print(K)
    for i in range(n + 1):
        for w in range(total_weight + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif item_weight[i - 1] <= w:
                K[i][w] = max(item_value[i - 1] + K[i - 1][w - item_weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][total_weight]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print(knapSack(W, wt, val))
