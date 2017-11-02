string1 = input("Enter string S1:")
string2 = input("Enter string S2:")
s2_len = len(string2)
s1_len = len(string1)
table = []
s3 = ''
for x in range(s1_len + 1):
    table.append([0] * (s2_len + 1))

def print_board(table):
    for row in table:
        print((row))

for i in range(1, s1_len + 1):
    for j in range(1, s2_len + 1):
        if string2[j - 1] == string1[i - 1]:
            table[i][j] = table[i - 1][j - 1] + 1
        else:
            table[i][j] = max(table[i - 1][j], table[i][j - 1])

# print_board(table)
i = s1_len
j = s2_len
while i > 0 and j > 0:
    if table[i][j] == table[i - 1][j]:
        i -= 1
    elif table[i][j] > table[i][j - 1]:
        s3 = s3 + string2[j - 1]
        j -= 1
        i -= 1
    else:
        j -= 1

# print(list(string2))
# print(len(table[0]), len(string2) + 1)
print(s3[::-1])
