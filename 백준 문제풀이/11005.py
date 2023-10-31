# 11005 - 진법 변환 2 

'''
10진수인 36을 2진법으로 출력하는 원리를 파악해보자
36 = 36 / 2 = 18 / 2 = 9 / 2 = 8(1) / 2 = 4 / 2 = 2 / 2 = 1

1 2 4 8 16 32 
0 0 1 0 0  1 

48 8진법

1 2 4 8 16 
0 0 0 0 1 

16 / 2 = 8 - 0
8 / 2 = 4 - 0 
4 /2 = 2 - 0
2/2 = 1 - 0 

'''
n,b = map(int,input().split())

convert_lst = '' 

while True :
  if n == 0 : 
   break   

  if n % b >= 10 :
    convert = chr(n % b + 55)
  else : 
    convert = n % b
  convert_lst.append(convert) # 리스트였을 경우 convert_lst.append(convert) 
  n = n // b # n / b 를 해서 0 조건식을 뒀을 때 끝도없이 수가 나왔던것 

 
# if n <= 1 보다 작을경우 break 하는 조건식일 경우 필요했던 구문
# 맨 마지막 인덱스가 0일 경우 출력하지 않는다. 
# if convert_lst[-1] == 0 : 
#   convert_lst.pop(-1)

for i in range(len(convert_lst)) : 
  print(convert_lst[(len(convert_lst)-1) - i], end='')

# 다른 사람 풀이 
N, B = map(int, input().split())
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N :
  s += str(arr[N%B]) # 나머지를 통해 인덱스를 출력하는 방법 
  N //= B 

print(s[::-1])