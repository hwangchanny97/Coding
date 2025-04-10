# https://www.acmicpc.net/problem/1316

N = int(input())
count = 0
for i in range(N):
    word = input()
    indexDict = {}
    isGroupWord = True
    for idx, c in enumerate(word):
        if c in indexDict and indexDict[c] != idx-1:
            isGroupWord = False
            break
        else:
            indexDict[c] = idx
    if isGroupWord:
        count += 1

print(count)


