# 2444 - 별 찍기 7

'''
1
3
5
7
9
7
5
3
1
'''

n = int(input())

j = n
k = -1

for i in range(n) :
  j -= 1 
  k += 2
  print(j*' '+(k*'*')) # 여기서 공백과 별 문자열 연결을 ','쉼표를 통해 했더니, 중간사이에 공백이 생겨서 계속 틀리다고 떴다. 그래서 문자열연결을 + 연산자를 사용해 공백을 지워주니 정답! 
   

for i in range(n-1) :
  j += 1 
  k -= 2 
  print(j*' '+(k*'*'))

# 다른 사람 풀이 

n = int(input())

for i in range(1,n+1) : 
  print(' '*(n-i)+'*'*(2*i-1))
for k in range(n-1,0,-1) : 
  print(' '*(n-k)+'*'*(2*k-1))  
