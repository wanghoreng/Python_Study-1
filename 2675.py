# 2675 번 
T = int(input())


for i in range(0,T) : 
  R,S = input().split() 
  for j in S : # S = ABC 
    for k in range(0,int(R)) : 
      print(j, end='')
  print()



