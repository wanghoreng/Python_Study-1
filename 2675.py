# 2675 번 
T = int(input())


for i in range(0,T) : 
  R,S = input().split() 
  for j in S : # S = ABC 
    for k in range(0,int(R)) : 
      print(j, end='')
  print()


# 결과 
'''
2                    
3 ABC
AAABBBCCC             - 결과
5 /HTP
/////HHHHHTTTTTPPPPP  - 결과 
'''