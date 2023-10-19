# 10811 - 바구니 뒤집기 

n,m = map(int,input().split())

# 번호가 순차적으로 늘어나는 바구니 만들기  
boxs = [x for x in range(1,n+1)]

num = []

for _ in range(m) : 
  i,j = map(int,input().split()) # 1 2 
  temp = boxs[i-1:j] 
  temp.reverse() # 뒤집기  
  boxs[i-1:j] = temp

for i in range(n):
  print(boxs[i],end=' ')

# reverse() 
'''
반복되는 리스트를 뒤집어 기존 리스트를 변경하여 반환값은 None 이다. 
'''



  