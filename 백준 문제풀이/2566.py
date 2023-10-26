# 2566 - 최대값 

arr = [[j for j in range(9)]for _ in range(9)]
result = 0 

for i in range(9) : 
    arr[i] = list(map(int,input().split()))
    
for i in range(9) : 
    for j in range(9) : 
        result = max(result,arr[i][j])
        
for i in range(9) : 
    if result in arr[i] :
      p1 = i
      p2 = arr[i].index(result)
    else : 
      pass
      

print(result)
print(p1+1,p2+1)
