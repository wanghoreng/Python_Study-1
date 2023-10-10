# 2839 번 문제 - 설탕 배달 

# 문제 요약 
'''
3과 5 킬로그램을 가진 설탕봉지가 있다.
N킬로그램을 배달해야한다고 가정할 때 
설탕봉지를 최대한 적게 들고 갈 수 있는 갯수를 구하는 문제이다. 
'''

n = int(input())

count = 0
while n!= 0 : 
  if n < 5 : 
    count = -1 
    break
  while n % 5 != 0 : 
    n -= 3
    count += 1  
  count += n // 5 

print(count) 