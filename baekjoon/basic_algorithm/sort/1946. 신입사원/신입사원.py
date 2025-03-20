import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  candidates = []

  for _ in range(N):
    s, m = map(int, input().split())
    candidates.append((s,m))
  # (s, m) pair의 정렬 -> 첫번째로 정렬하고 같다면 두번째거로 정렬
  candidates.sort()
  
  top_ranking = 1e9
  count = 0
  
  for i in range(N):
    if candidates[i][1] < top_ranking:
      count += 1
      top_ranking = candidates[i][1]
    
  print(count)