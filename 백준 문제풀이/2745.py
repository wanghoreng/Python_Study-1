# 2745 - 진법 변환

'''
ZZZZZ(36)  

Z = 35 

 35 * (36**4)
+ 35 * (36**3)
+ 35 * (36**2)
+ 35 * (36**1)
+ 35 * (36**0)
---------------
=> 10진법 변환 완료
'''

# print(ord('A')) # 65 - 55 = 10
# print(ord('Z')) # 90 - 55 = 35


import sys

n,b = sys.stdin.readline().split()
sum = 0

for i in range(len(n)) : # 0 ~ 문자열길이까지 
  if (n[(len(n)-1)-i].isdigit()) :  # 숫자일경우 1의 자리부터 
    sum += int(n[(len(n)-1)-i]) * (int(b)**i)
  else :  # 문자일경우 -55
    sum += (ord(n[(len(n)-1)-i])-55) * (int(b)**i)

print(sum)

# 처음 알게된 함수 
'''
isdigit() : 어떤 문자열이 숫자의 형태면 True 를 반환

이와 비슷한 함수 종류 
isdecimal() : 어떤 문자열이 int 형으로 변환이 가능하면 True 
isnumeric() : 숫자값 표현에 해당하는 문자열이면 True 
isalpha() : 문자열이 알파벳으로만 구성되어 있다면 True, 공백이나 숫자의 형태로 변환가능한 문자라면 False 반환 
'''

# 다른 사람 풀이 
n,b = input().split()

print(int(n, int(b)))
'''
파이썬의 int 함수는 임의의 진법 수를 10진법으로 변환하는데 사용할 수 있다.
즉, int('ZZZZZ', 36) 형식은 36진법으로 이루어진 'ZZZZZ'를 10진법으로 변환한다는 의미이다. 
'''
