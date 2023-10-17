# 10810 - 공 넣기 문제 

# 문제 접근 방식
'''
간단하게 배열을 하나 만들고,
입력받은 대로 배열에 넣기만 하면 되는 문제이다. 
기존에 있던 공을 뺀다는 조건은, 그냥 해당 값을 덮어씌우면 되기 때문이다.
'''

n,m = map(int,input().split())

box = [0 for _ in range(n)]

for _ in range(m) : 
  i,j,k = map(int,input().split())
  for ball in range(i-1,j) : 
    box[ball] = k 


for i in box : 
  print(i,end=' ')