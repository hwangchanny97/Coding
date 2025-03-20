N, M = map(int, input().split())
video = list(map(int, input().split()))
#del sum


left = max(video)
right = sum(video)

while left <= right:
  middle = (left + right) // 2 # 임시 블루레이 용량

  blueray_num = 1   # 블루레이 갯수
  remain = middle   # 남은 시간

  for i in range(N):      
    if remain < video[i]:   # 비디오 크기보다 블루레이 디스크 남는 공간이 적다면 다음 블루레이 할당
      blueray_num += 1
      remain = middle       # 다시 블루레이의 크기만큼 할당됨

    remain -= video[i]      # 블루레이 크기에서 비디오 크기 빼기
  
  if blueray_num <= M:      # 블루레이가 블루레이 최대 갯수보다 작거나 같다면 
    answer = middle         # 임시 답은 middle이 됨
    right = middle -1       # [left, middle -1]
  else:
    left = middle + 1       # [middle + 1, right]
  
print(answer)