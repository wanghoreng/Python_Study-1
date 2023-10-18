# 10813 - 공 바꾸기 

n,m = map(int,input().split())

# 1부터 n 까지의 바구니와 그 안의 공 값 넣기
boxs = [x for x in range(1,n+1)]

# m번 교환
for _ in range(m) : 
  i,j = map(int,input().split())
  # 임시공간에 담기
  temp = boxs[i-1] #인덱스는 0부터 시작이므로 -1
  boxs[i-1] = boxs[j-1]
  boxs[j-1] = temp 

for box in boxs : 
  print(box,end=' ')