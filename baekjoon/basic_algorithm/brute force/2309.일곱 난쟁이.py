from itertools import combinations

heights = []

for i in range(9):
    height = int(input())
    heights.append(height)

print(heights)

for a in combinations(heights, 7):
    print(a)
    if sum(a) == 100:
        a = list(a)
        a.sort()
        for x in a:
            print(x)
        break

    